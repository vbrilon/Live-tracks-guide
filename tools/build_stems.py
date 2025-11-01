#!/usr/bin/env python3
"""
Build 48k/24-bit WAV stems (+ click/cues) from per-instrument MP3s.

Inputs
- Root folder containing one folder per song (e.g., ~/Dropbox/Song_Tracks)
- Each song folder contains multiple .mp3 files (one per instrument) and a click mp3

Outputs
- LiveTracks/Songs/<SongName>/Stems/
  - 13_Click.wav, 14_Cues.wav (if present)
  - 15_TracksA.wav, 16_TracksB.wav, 17_TracksC.wav, 18_TracksD.wav

Dependencies
- ffmpeg installed and on PATH (brew install ffmpeg)

Usage
  python3 tools/build_stems.py \
    --root "~/Dropbox/Song_Tracks" \
    --out  "./LiveTracks/Songs" \
    [--map tools/keywords.yml] \
    [--dry-run]

Classification
- Files are grouped into A/B/C/D by filename keywords (case-insensitive). You can
  customize patterns in tools/keywords.yml. Unknowns fall back to TracksA.

Mixing
- For each group, inputs are mixed with amix normalize=1 and limited (TP ~ -1dB).
- All outputs are 48kHz, PCM 24-bit WAV (pcm_s24le).
"""
import argparse
import os
import re
import shlex
import subprocess
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    yaml = None


DEFAULT_MAP = {
    "click": [r"click"],
    "cues": [r"cue", r"cues", r"guide", r"count", r"vox.?cue"],
    # Perc/Loops/Drums
    "A": [
        r"drum", r"perc", r"loop", r"shaker", r"tamb", r"clap", r"kick", r"snare",
        r"tom", r"oh", r"overhead", r"hihat", r"hi.?hat", r"cym", r"808|909"
    ],
    # Synth/Bass/Gtr
    "B": [r"bass", r"synth[-_ ]?bass", r"gtr|guitar", r"lead", r"mono", r"arp"],
    # Keys/Pads
    "C": [r"keys?", r"pad", r"piano", r"rhodes", r"organ", r"strings", r"synth\s*pad"],
    # BGV/FX
    "D": [r"bgv|back(ing)?.?vox", r"harm|harmony|choir", r"fx|sfx", r"swell|stab"],
}


def load_map(path: Path | None):
    if not path:
        return DEFAULT_MAP
    if not yaml:
        raise SystemExit("PyYAML not available; remove --map or install pyyaml")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    mapping = DEFAULT_MAP.copy()
    mapping.update({k: v for k, v in data.items() if isinstance(v, list)})
    return mapping


def classify(file: Path, mapping: dict[str, list[str]]):
    name = file.name.lower()
    # Click / Cues take precedence
    for tag in ("click", "cues"):
        for pat in mapping.get(tag, []):
            if re.search(pat, name):
                return tag
    # Stems A-D
    for stem in ("A", "B", "C", "D"):
        for pat in mapping.get(stem, []):
            if re.search(pat, name):
                return stem
    return "A"


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def run(cmd: str):
    print(f"$ {cmd}")
    res = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0:
        raise RuntimeError(res.stderr.decode("utf-8", errors="ignore"))


def decode_to_wav(src: Path, dst: Path):
    # 48k, 24-bit PCM
    cmd = f"ffmpeg -y -hide_banner -loglevel error -i {shlex.quote(str(src))} -ar 48000 -c:a pcm_s24le {shlex.quote(str(dst))}"
    run(cmd)


def mix_group(inputs: list[Path], out_wav: Path):
    if not inputs:
        return
    if len(inputs) == 1:
        decode_to_wav(inputs[0], out_wav)
        return
    # Build amix filter with normalize and limiter
    inputs_quoted = " ".join(shlex.quote(str(p)) for p in inputs)
    # Use amerge? We'll use amix to sum; normalize=1 scales by number of inputs, then limit peaks.
    filter_complex = "amix=inputs=%d:normalize=1,alimiter=limit=-1.0dB" % len(inputs)
    cmd = f"ffmpeg -y -hide_banner -loglevel error " \
          f"{' '.join(['-i '+shlex.quote(str(p)) for p in inputs])} " \
          f"-filter_complex {shlex.quote(filter_complex)} -ar 48000 -c:a pcm_s24le {shlex.quote(str(out_wav))}"
    run(cmd)


def process_song(song_dir: Path, out_root: Path, mapping: dict[str, list[str]], dry: bool = False):
    files = [p for p in sorted(song_dir.glob("*.mp3")) if p.is_file()]
    if not files:
        return
    buckets: dict[str, list[Path]] = {"click": [], "cues": [], "A": [], "B": [], "C": [], "D": []}
    for f in files:
        tag = classify(f, mapping)
        buckets[tag].append(f)
    # Prepare output folder
    stems_dir = out_root / song_dir.name / "Stems"
    ensure_dir(stems_dir)
    print(f"\n== {song_dir.name} ==")
    for k, v in buckets.items():
        print(f"  {k}: {len(v)} file(s)")
    if dry:
        return
    # Click
    if buckets["click"]:
        decode_to_wav(buckets["click"][0], stems_dir / "13_Click.wav")
    # Cues (optional)
    if buckets["cues"]:
        decode_to_wav(buckets["cues"][0], stems_dir / "14_Cues.wav")
    # Stems A-D
    mix_group(buckets["A"], stems_dir / "15_TracksA.wav")
    mix_group(buckets["B"], stems_dir / "16_TracksB.wav")
    mix_group(buckets["C"], stems_dir / "17_TracksC.wav")
    mix_group(buckets["D"], stems_dir / "18_TracksD.wav")


def main():
    ap = argparse.ArgumentParser(description="Build 48k/24-bit WAV stems from per-instrument mp3s (by folder)")
    ap.add_argument("--root", required=True, help="Root folder with one subfolder per song (source .mp3s)")
    ap.add_argument("--out", required=True, help="Output root for LiveTracks/Songs/<Song>/Stems")
    ap.add_argument("--map", help="YAML file with keyword mapping (overrides defaults)")
    ap.add_argument("--dry-run", action="store_true", help="Only print classification; do not render audio")
    args = ap.parse_args()

    src_root = Path(os.path.expanduser(args.root)).resolve()
    out_root = Path(os.path.expanduser(args.out)).resolve()
    mapping = load_map(Path(args.map).resolve()) if args.map else load_map(None)

    if not src_root.exists():
        raise SystemExit(f"Source root not found: {src_root}")
    ensure_dir(out_root)

    song_dirs = [p for p in sorted(src_root.iterdir()) if p.is_dir()]
    if not song_dirs:
        raise SystemExit("No song folders found")

    for d in song_dirs:
        process_song(d, out_root, mapping, dry=args.dry_run)

    print("\nDone. Import the WAVs in each Stems folder into Ableton as Scenes (one row per song).")


if __name__ == "__main__":
    main()

