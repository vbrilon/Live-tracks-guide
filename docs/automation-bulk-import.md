[Home](../README.md) · [Getting Started](getting-started.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md)
[Also see: Tempo Map From Click](tempo-map-from-click.md)

# Automation: Bulk Import MP3 Song Folders → Ableton Scenes

Goal: You have ~30 songs in `~/Dropbox/Song_Tracks/<SongName>/*.mp3`, one file per instrument plus a click track (all aligned). This automation builds standard 48k/24‑bit WAV stems (Click, Cues, Tracks A–D) for each song, then imports them into a single Ableton set (one Scene per song).

Outcome
- For each song: `LiveTracks/Songs/<SongName>/Stems/13_Click.wav, 14_Cues.wav, 15_TracksA.wav, 16_TracksB.wav, 17_TracksC.wav, 18_TracksD.wav`
- In Ableton: one Scene per song with these six clips mapped to `Ext. Out 13–18`.

## Step 1 — Build stems from MP3s (ffmpeg)

Prereqs
- Install ffmpeg (macOS): `brew install ffmpeg`

Classify + render
- Optionally edit `tools/keywords.yml` to tune how filenames map to A/B/C/D.
- Run (dry‑run first):
  - `python3 tools/build_stems.py --root "~/Dropbox/Song_Tracks" --out "./LiveTracks/Songs" --map tools/keywords.yml --dry-run`
- Render audio:
  - `python3 tools/build_stems.py --root "~/Dropbox/Song_Tracks" --out "./LiveTracks/Songs" --map tools/keywords.yml`

Notes
- Click/Cues: if multiple matches, the first is used. Cues are optional.
- Mixing: groups are summed with `amix=normalize=1` and peak‑limited (TP ≈ −1 dB). Outputs are 48 kHz / 24‑bit WAV.
- You can re‑run safely; outputs overwrite.

### Adding vocal cues (options)
- Record method (fastest): While listening to the song, record “Verse two three four”, “Chorus”, etc., on your phone. Export the file as `<SongName>_cues.mp3` into the song’s source folder. The build script will detect it and convert to `14_Cues.wav`.
- TTS method (automated): Create `LiveTracks/Songs/<SongName>/cues.yml` with time‑stamped events (see `tools/cues-template.yml`). Then run:
  - `python3 tools/build_cues.py --songs ./LiveTracks/Songs`
  This generates `14_Cues.wav` per song using macOS `say` and ffmpeg.
  - Note: Keep cues sparse and clear; avoid crowding the band’s ears.

## Step 2 — Create/prepare Ableton set

- In Ableton, create audio tracks named `Click`, `Cues`, `Tracks 1`, `Tracks 2`, `Tracks 3`, `Tracks 4`.
- Set `Audio To`:
  - Click → `Ext. Out 13`
  - Cues → `Ext. Out 14`
  - Tracks 1 → `Ext. Out 15`
  - Tracks 2 → `Ext. Out 16`
  - Tracks 3 → `Ext. Out 17`
  - Tracks 4 → `Ext. Out 18`
- Preferences → Record/Warp/Launch: disable “Auto‑Warp Long Samples”.
- Set Global Quantization to 1 Bar.

## Step 3 — Import all songs as Scenes (fast manual)

Add the folder
- In Ableton’s Browser, right‑click “Places” → Add Folder → select `LiveTracks/Songs`.

For each song folder
- Select the next empty Scene row in Session View.
- In Browser, open the song’s `Stems/` and sort ascending by name so 13_.. → 18_.. order.
- Select all six files and press Enter. Live will place them left‑to‑right into the selected row’s clip slots.
- Rename the Scene to `01 <SongName>` (use numbers for order).

Tips (speed)
- Use keyboard focus: Up/Down to move Scenes, Enter to place.
- Color each Scene; use Stop buttons for empty clip slots.

### Step 3b — Add per‑song MIDI clip (optional)
- Create a `MIDI Out` track and set `MIDI To` to `IAC Driver (Bus 1)` or your hardware MIDI port.
- If a per‑song MIDI file exists (e.g., `<SongName>.mid`), drag it into the `MIDI Out` clip slot in that song’s Scene row.
- Global Quantization at 1 Bar keeps MIDI/audio launches aligned.

Optional: automate the import (Keyboard Maestro)
- You can build a macro that loops song folders in the Browser, presses Enter on the next Scene, then moves down. Record the keystrokes; add small delays.

## Variations

- Dedicated channels (6, 7, 12): If a live player is missing, add dedicated Ableton tracks for Bass (6), Guitar (7), Keys (12). Remove that instrument from A–D so it isn’t doubled, and route its track to the dedicated output.
- Drum tracks mono/stereo: If you want a mono drum stem on ch 4 or stereo on 4/5 (no live drummer), render those variants with the `tools/build_stems.py` by mapping drum files to C and retargeting. Or use the Reaper Batch Prep pipeline to generate 1–5 multi‑stems if needed.
 - MIDI batch naming: Keep per‑song MIDI files as `<SongName>.mid` inside each `Stems/` or song folder to speed drag‑in to the `MIDI Out` track.

## Troubleshooting

- Wrong files in A/B/C/D: tune `tools/keywords.yml` and re‑run.
- Clipping or low level: stems use amix normalization + limiter; adjust per‑stem clip gain in Ableton as needed.
- Timing drift: ensure Auto‑Warp is off; if the source MP3 drifts, consider the Logic/Reaper tempo map route to print a more reliable click/cues.
 - Need a bar‑aligned grid to place cues/MIDI? Generate `tempo.mid` from the click first: see [Tempo Map From Click](tempo-map-from-click.md).
