#!/usr/bin/env python3
"""
Synthesize vocal cues per song from time-stamped text events using macOS TTS (say).

Inputs
- LiveTracks/Songs/<SongName>/cues.yml with:

  voice: Samantha   # optional; any macOS voice
  events:
    - at: "0:07.0"  # mm:ss(.mmm)
      text: "Verse – two three four"
    - at: "0:35.0"
      text: "Chorus"

Outputs
- LiveTracks/Songs/<SongName>/Stems/14_Cues.wav (48k/24-bit, mono)

Requires
- macOS `say` command
- ffmpeg on PATH (brew install ffmpeg)
"""
import argparse
import os
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    yaml = None


def run(cmd: str):
    print(f"$ {cmd}")
    res = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0:
        raise RuntimeError(res.stderr.decode("utf-8", errors="ignore"))


def parse_time_to_ms(s: str) -> int:
    s = s.strip()
    parts = s.split(":")
    if len(parts) == 2:
        m, rest = parts
        sec = float(rest)
        return int(round((int(m) * 60 + sec) * 1000))
    if len(parts) == 3:
        h, m, rest = parts
        sec = float(rest)
        return int(round(((int(h) * 60 + int(m)) * 60 + sec) * 1000))
    # seconds only
    return int(round(float(s) * 1000))


def synth_tts(text: str, voice: str | None, out_aiff: Path):
    voice_arg = ["-v", voice] if voice else []
    cmd = ["say", *voice_arg, "-o", str(out_aiff), text]
    print("$ ", " ".join(shlex.quote(c) for c in cmd))
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0:
        raise RuntimeError(res.stderr.decode("utf-8", errors="ignore"))


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def process_song(song_dir: Path, overwrite: bool = False):
    cues_yml = song_dir / "cues.yml"
    stems_dir = song_dir / "Stems"
    if not cues_yml.exists():
        return False
    if not stems_dir.exists():
        print(f"Warning: Stems folder not found for {song_dir.name}; creating {stems_dir}")
        ensure_dir(stems_dir)
    if not yaml:
        raise SystemExit("PyYAML not installed; install with 'pip install pyyaml' or use recorded cues mp3.")
    data = yaml.safe_load(cues_yml.read_text(encoding="utf-8")) or {}
    voice = data.get("voice")
    events = data.get("events") or []
    if not events:
        print(f"No events in {cues_yml}")
        return False
    out_wav = stems_dir / "14_Cues.wav"
    if out_wav.exists() and not overwrite:
        print(f"Exists (skip): {out_wav}")
        return False

    with tempfile.TemporaryDirectory() as td:
        seg_paths = []
        delays = []
        for idx, ev in enumerate(events):
            at = ev.get("at")
            text = (ev.get("text") or "").strip()
            if not at or not text:
                continue
            ms = parse_time_to_ms(str(at))
            aiff = Path(td) / f"seg_{idx:03d}.aiff"
            wav = Path(td) / f"seg_{idx:03d}.wav"
            synth_tts(text, voice, aiff)
            # Convert to WAV mono 48k/24-bit
            run(f"ffmpeg -y -hide_banner -loglevel error -i {shlex.quote(str(aiff))} -ac 1 -ar 48000 -c:a pcm_s24le {shlex.quote(str(wav))}")
            seg_paths.append(wav)
            delays.append(ms)

        # Build filter graph with adelay per segment then amix
        if not seg_paths:
            print(f"No valid segments for {song_dir.name}")
            return False
        inputs = " ".join(f"-i {shlex.quote(str(p))}" for p in seg_paths)
        chains = []
        labels = []
        for i, ms in enumerate(delays):
            lbl = f"a{i}"
            labels.append(f"[{lbl}]")
            chains.append(f"[{i}:a]adelay={ms}|{ms}[{lbl}]")
        amix = f"{''.join(labels)}amix=inputs={len(seg_paths)}:normalize=0,alimiter=limit=-1.0dB"
        filt = ";".join(chains + [amix])
        ensure_dir(out_wav.parent)
        cmd = f"ffmpeg -y -hide_banner -loglevel error {inputs} -filter_complex {shlex.quote(filt)} -ar 48000 -c:a pcm_s24le {shlex.quote(str(out_wav))}"
        run(cmd)
    print(f"Wrote {out_wav}")
    return True


def main():
    ap = argparse.ArgumentParser(description="Build 14_Cues.wav using macOS TTS from cues.yml files")
    ap.add_argument("--songs", required=True, help="Root folder LiveTracks/Songs")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing 14_Cues.wav")
    args = ap.parse_args()
    songs_root = Path(os.path.expanduser(args.songs)).resolve()
    if not songs_root.exists():
        raise SystemExit(f"Songs root not found: {songs_root}")
    any_done = False
    for song_dir in sorted(p for p in songs_root.iterdir() if p.is_dir()):
        try:
            if process_song(song_dir, overwrite=args.overwrite):
                any_done = True
        except Exception as e:
            print(f"Error: {song_dir.name}: {e}")
    if not any_done:
        print("No cues built. Ensure cues.yml exists in song folders.")


if __name__ == "__main__":
    if sys.platform != "darwin":
        print("Warning: build_cues.py uses macOS 'say'. Run on macOS or record cues manually.")
    main()

