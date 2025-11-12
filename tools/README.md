# Tools Index

Purpose: quick reference for repo automation tools with inputs/outputs and example commands.

## build_stems.py — MP3 folders → 48k/24‑bit WAV stems

- Input: one folder per song containing per‑instrument `.mp3` files and a click/cues mp3.
- Output: `LiveTracks/Songs/<Song>/Stems/` with:
  - `13_Click.wav`, `14_Cues.wav` (if present)
  - `15_TracksA.wav`, `16_TracksB.wav`, `17_TracksC.wav`, `18_TracksD.wav`
- Mapping: filenames are classified into A/B/C/D by keywords (configurable via `tools/keywords.yml`). Unknowns fall back to A.
- Dependencies: `ffmpeg`
- Examples
  - Dry‑run: `python3 tools/build_stems.py --root "~/Dropbox/Song_Tracks" --out "./LiveTracks/Songs" --map tools/keywords.yml --dry-run`
  - Render:  `python3 tools/build_stems.py --root "~/Dropbox/Song_Tracks" --out "./LiveTracks/Songs" --map tools/keywords.yml`

## click_to_tempo.py — Build `tempo.mid` from click audio

- Input: `LiveTracks/Songs/<Song>/Stems/13_Click.wav` (or override via `--click`).
- Output: `LiveTracks/Songs/<Song>/tempo.mid` with SetTempo and Time Signature events.
- Why: author cues/MIDI precisely on a bar grid in a DAW, then export audio cues for Ableton Session (Warp Off).
- Dependencies: `ffmpeg`, `aubio` CLI, Python `mido`
- Examples
  - All songs:  `python3 tools/click_to_tempo.py --songs ./LiveTracks/Songs --meter 4/4`
  - Single song: `python3 tools/click_to_tempo.py --song ./LiveTracks/Songs/MySong --meter 6/8`

## build_cues.py — Synthesize `14_Cues.wav` from `cues.yml` (macOS)

- Input: `LiveTracks/Songs/<Song>/cues.yml` with `voice:` and time‑stamped `events:`
- Output: `LiveTracks/Songs/<Song>/Stems/14_Cues.wav` (48 kHz / 24‑bit, mono)
- Dependencies: macOS `say`, `ffmpeg`, Python `PyYAML`
- Example
  - `python3 tools/build_cues.py --songs ./LiveTracks/Songs`

## keywords.yml — Filename → stem group mapping

- Structure: lists of case‑insensitive regex fragments per group.
- Keys: `click`, `cues`, `A`, `B`, `C`, `D`.
- Tip: keep patterns simple and mutually exclusive when possible.

## cues-template.yml — Starter for `cues.yml`

- Copy to `LiveTracks/Songs/<Song>/cues.yml` and edit text/timestamps.

See also
- Bootstrap script: `scripts/bootstrap-mac.sh`
- Tempo map guide: `docs/tempo-map-from-click.md`
- Bulk import: `docs/automation-bulk-import.md`
