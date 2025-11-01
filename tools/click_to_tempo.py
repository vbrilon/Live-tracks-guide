#!/usr/bin/env python3
"""
Generate a MIDI tempo map (tempo.mid) from an audio click track.

Approach
- Uses aubio's beat tracker to detect beat times from the click audio.
- Creates a Standard MIDI File (SMF) with SetTempo meta events at each beat start,
  where tempo (us/qn) = measured beat duration * 1e6. This yields a bar/beat grid
  that matches the original click timing in DAWs that import tempo from MIDI.

Inputs
- Song root containing Stems/13_Click.wav (or any audio file via --click).
- Optional per-song YAML for meter settings (numerator/denominator).

Outputs
- <SongDir>/tempo.mid (tempo + time signature track)

Requirements
- ffmpeg (for transcoding non-WAV input) — brew install ffmpeg
- aubio CLI (for beat tracking) — brew install aubio
- Python: mido — pip install mido

Usage
  python3 tools/click_to_tempo.py --songs ./LiveTracks/Songs [--meter 4/4]
  python3 tools/click_to_tempo.py --song ./LiveTracks/Songs/MySong --click path/to/click.wav --meter 4/4

Notes
- The first detected beat becomes bar 1 beat 1. If your click file starts before bar 1
  (e.g., with a count-in), import the tempo.mid and adjust the bar offset in your DAW.
"""
from __future__ import annotations
import argparse
import os
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import mido  # type: ignore
except Exception as e:
    print("Error: Python package 'mido' is required. Install with 'pip install mido'.")
    raise


PPQ = 480  # ticks per quarter note


@dataclass
class Meter:
    num: int = 4
    den: int = 4

    @staticmethod
    def parse(s: str | None) -> "Meter":
        if not s:
            return Meter()
        m = re.match(r"^(\d+)\s*/\s*(\d+)$", s.strip())
        if not m:
            raise ValueError(f"Invalid meter '{s}', expected like 4/4, 3/4, 6/8")
        num = int(m.group(1)); den = int(m.group(2))
        if den not in (1, 2, 4, 8, 16, 32):
            raise ValueError("Denominator must be a power of two (1,2,4,8,16,32)")
        return Meter(num, den)


def run(cmd: str) -> str:
    print(f"$ {cmd}")
    res = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0:
        err = res.stderr.decode("utf-8", errors="ignore")
        raise RuntimeError(err)
    return res.stdout.decode("utf-8", errors="ignore")


def ensure_wav(click_path: Path) -> Path:
    if click_path.suffix.lower() == ".wav":
        return click_path
    out = click_path.with_suffix(".tmp.wav")
    run(f"ffmpeg -y -hide_banner -loglevel error -i {shlex.quote(str(click_path))} -ac 1 -ar 48000 {shlex.quote(str(out))}")
    return out


def aubio_beats(wav_path: Path) -> list[float]:
    # Use aubio's tempo tracker to print beat times
    # Example output lines: "0.500000\n1.000000\n..."
    txt = run(f"aubio tempo -i {shlex.quote(str(wav_path))}")
    beats = []
    for line in txt.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            t = float(line)
            beats.append(t)
        except ValueError:
            continue
    # Deduplicate/monotonic
    beats = sorted(set(beats))
    # Remove the temporary last beat if aubio printed trailing zeros
    return beats


def write_tempo_midi(beats: list[float], meter: Meter, out_mid: Path):
    if len(beats) < 2:
        raise ValueError("Not enough beats detected to build a tempo map")
    mid = mido.MidiFile(type=1)
    mid.ticks_per_beat = PPQ
    track = mido.MidiTrack()
    mid.tracks.append(track)
    # Write initial time signature at tick 0
    # mido time_signature: time_signature(numerator, denominator, clocks_per_click=24, notated_32nd_notes_per_beat=8)
    track.append(mido.MetaMessage('time_signature', numerator=meter.num, denominator=meter.den, time=0))
    prev_tick = 0
    # For each beat boundary i, compute tempo = (t[i+1]-t[i]) seconds per beat
    for i in range(len(beats) - 1):
        dt_sec = max(1e-6, beats[i+1] - beats[i])
        us_per_beat = int(dt_sec * 1_000_000)
        event_tick = i * PPQ
        delta = event_tick - prev_tick
        track.append(mido.MetaMessage('set_tempo', tempo=us_per_beat, time=delta))
        prev_tick = event_tick
    # End of track
    track.append(mido.MetaMessage('end_of_track', time=PPQ))
    out_mid.parent.mkdir(parents=True, exist_ok=True)
    mid.save(out_mid)
    print(f"Wrote {out_mid}")


def process_song(song_dir: Path, meter: Meter, click_override: Path | None = None):
    # Prefer Stems/13_Click.wav, else override
    if click_override:
        click_path = click_override
    else:
        click_path = song_dir / "Stems" / "13_Click.wav"
        if not click_path.exists():
            # Fallback: any file with 'click' in name
            cand = next((p for p in song_dir.glob("**/*") if p.is_file() and 'click' in p.name.lower()), None)
            if not cand:
                raise FileNotFoundError(f"No click file found in {song_dir}")
            click_path = cand
    wav = ensure_wav(click_path)
    beats = aubio_beats(wav)
    if wav.suffix == ".tmp.wav":
        try:
            wav.unlink()
        except Exception:
            pass
    out_mid = song_dir / "tempo.mid"
    write_tempo_midi(beats, meter, out_mid)


def main():
    ap = argparse.ArgumentParser(description="Generate tempo.mid from click audio using aubio")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--songs", help="Root folder containing LiveTracks/Songs/<SongName>")
    g.add_argument("--song", help="Single song folder (LiveTracks/Songs/<SongName>)")
    ap.add_argument("--click", help="Override click audio path for single-song mode")
    ap.add_argument("--meter", help="Time signature, e.g., 4/4 (default), 3/4, 6/8")
    args = ap.parse_args()
    meter = Meter.parse(args.meter)

    if args.song:
        process_song(Path(os.path.expanduser(args.song)).resolve(), meter, Path(os.path.expanduser(args.click)).resolve() if args.click else None)
        return
    songs_root = Path(os.path.expanduser(args.songs)).resolve()
    for song_dir in sorted(p for p in songs_root.iterdir() if p.is_dir()):
        try:
            process_song(song_dir, meter)
        except Exception as e:
            print(f"Skip {song_dir.name}: {e}")


if __name__ == "__main__":
    # Pre-flight checks for aubio
    try:
        run("aubio tempo -h")
    except Exception:
        print("Error: 'aubio' CLI not found. Install with 'brew install aubio' (macOS).")
        sys.exit(1)
    main()

