[Home](../README.md) · [Getting Started](getting-started.md) · [Tracks Prep](tracks-prep.md) · [Automation (Bulk Import)](automation-bulk-import.md) · [Reaper Batch Prep](reaper-batch-prep.md)

# Tempo Map From Click (Automatic)

Goal: Build a tempo map (tempo.mid) from each song’s click audio so your DAW’s bar/beat grid aligns exactly. This lets you place cues and MIDI on the grid quickly, then export audio cues for Ableton.

Two paths
- CLI (automated): Use aubio + Python to generate tempo.mid per song from 13_Click.wav.
- Reaper + SWS (GUI): Use Reaper to detect beats from the click and write the tempo map.

## Option A — CLI (aubio + Python)

Prereqs
- ffmpeg: `brew install ffmpeg`
- aubio: `brew install aubio`
- Python mido: `pip install mido`

Generate tempo.mid per song
- Ensure you have `LiveTracks/Songs/<Song>/Stems/13_Click.wav` (or source click mp3).
- Run for all songs:
  - `python3 tools/click_to_tempo.py --songs ./LiveTracks/Songs --meter 4/4`
- Or single song:
  - `python3 tools/click_to_tempo.py --song ./LiveTracks/Songs/MySong --meter 4/4`

Result
- `LiveTracks/Songs/<Song>/tempo.mid` with SetTempo + Time Signature.
- The first detected beat is bar 1. If your click starts with a count-in before bar 1, adjust bar offset in your DAW after import.

Use the tempo map
- Ableton: Drag `tempo.mid` into Arrangement; Live creates a Master tempo envelope and time-signature markers. You can now place cues/MIDI on the grid. Export 14_Cues.wav from Arrangement and use it in Session.
- Reaper: Import `tempo.mid` into a project; its tempo markers align the grid to your click.

Notes
- This method sets tempo at every beat based on measured inter-beat durations; it handles drift and variable tempo.
- If your meter is not 4/4, pass `--meter 3/4`, `6/8`, etc. You can change meter markers later in your DAW if needed.

Author and test a per‑song MIDI track
- After importing `tempo.mid`, create a `MIDI Out` track in your DAW.
- Place MIDI notes, Program Changes (PC), Control Changes (CC), or SysEx on bar/beat positions as needed.
- For Ableton testing: route `MIDI To` to `IAC Driver (Bus 1)` (macOS) or your hardware MIDI port. Use an `External Instrument` device to monitor the target synth if desired.
- When done, export a per‑song MIDI file (e.g., `<SongName>.mid`) to drop into the Ableton Session’s `MIDI Out` track for live playback.

## Option B — Reaper + SWS (GUI)

Prereqs
- Reaper + SWS Extensions installed.

Steps (per song; fast and repeatable)
1) Import the click audio.
2) Detect beats: Item → Dynamic split items → create stretch markers at transients (don’t split). Set threshold so you get one marker per beat.
3) Build tempo map: run SWS/BR action “Convert stretch markers to tempo markers / align grid to stretch markers (detect tempo)”.
4) Set the time signature marker at bar 1 (e.g., 4/4) and adjust bar offset if needed.
5) Export: File → Export Project MIDI → Embed tempo/time signature → `tempo.mid`.

Author cues on the grid
- With the tempo map active, add a `14_Cues` track and place cue one-shots or recorded voice items snapped to bars/beats. Render/bounce `14_Cues.wav` at 48 kHz / 24‑bit.

Next steps
- Drop `14_Cues.wav` into each song’s `Stems` and continue with the bulk import into Ableton Session.
