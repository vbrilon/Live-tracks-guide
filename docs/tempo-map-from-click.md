[Home](../README.md) · [Getting Started](getting-started.md) · [Tracks Prep](tracks-prep.md) · [Automation (Bulk Import)](automation-bulk-import.md) · [Reaper Batch Prep](reaper-batch-prep.md)

# Tempo Map From Click (Automatic)

Summary: Build tempo.mid from click audio so a DAW’s bar/beat grid matches the song; place cues/MIDI precisely, then export audio cues for Ableton.

Goal: Build a tempo map (tempo.mid) from each song’s click audio so your DAW’s bar/beat grid aligns exactly. This lets you place cues and MIDI on the grid quickly, then export audio cues for Ableton.

## Tempo Maps 101 (What, Why, Where)

- What it is: a list of tempo and time‑signature events (typically stored in a small MIDI file like `tempo.mid`). When imported into a DAW, these events make the bar/beat grid line up with the music—even if the song drifts or changes tempo/meter.
- Why it matters here: you author cues and any per‑song MIDI against a reliable musical grid, then export those cues to audio for live use. At show time in Ableton Session, you run all audio with Warp Off; the audio click/cues remain the single source of truth for timing.
- Where it’s used: in a DAW’s Arrangement/Timeline view (Ableton Arrangement, Logic, Reaper). Ableton Session Scenes don’t carry a changing tempo envelope—only a single BPM per Scene—so treat the tempo map as an authoring tool, not a runtime dependency.
- When you can skip it: steady‑tempo songs already on‑grid at 48 kHz with simple cues. You can place cues by ear and keep everything unwarped.
- When you should use it: any drift, rubato, meter/tempo changes, tight bar‑aligned cues, or when placing precise MIDI (PC/CC) tied to musical sections.

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

Consistent count‑in (2‑bar pre‑roll)
- Recommended convention (simple, consistent): place the first musical downbeat at bar 3, and use bars 1–2 for click pre‑roll and an optional spoken count‑in. When exporting, include bars 1–2 so every stem starts at bar 1. Click/Cues contain sound in bars 1–2; other stems contain silence for bars 1–2.
- Alternative (advanced): keep the first musical downbeat at bar 1 and use “negative bars”/bar offset for the count‑in. Not all users like working with negative bars; if you choose this, still export with two bars of pre‑roll so stems align in Ableton Session.
- CLI path tip: if using `click_to_tempo.py`, it’s fine if the `13_Click.wav` includes the two pre‑roll bars—the tempo map will include them. If it doesn’t, import `tempo.mid` and set the bar‑1 marker to your musical downbeat, then add two bars before it and export stems with the pre‑roll.

Quick sanity check (after import)
- Drop the original `13_Click.wav` on a track in the same project.
- Zoom to bar 1: the accented click should land on beat 1. If there’s a count‑in before bar 1, set bar‑1 marker and adjust bar offset so downbeats line up.
- Scrub through a few sections (Verse/Chorus/Bridge) and confirm downbeats continue to line up with click accents.
- Only after this alignment, place and export `14_Cues.wav` snapped to bars.

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

## Pitfalls & Fixes

- Bar‑1 offset and count‑ins: If the first strong click is a count‑in before the song, set bar‑1 at the first downbeat and adjust the bar offset after importing `tempo.mid`.
- Double/half‑time detection: If a detector locks to every 8th or every 2 bars, halve or double the resulting tempos, or tweak thresholds and re‑analyze. Always verify the bar‑1 accent and downbeats.
- Meter changes: Pass `--meter` (e.g., `3/4`, `6/8`) for CLI detection, then add/edit time‑signature markers in your DAW where the meter changes.
- Swing/triplet clicks: Automatic beat detection can drift. Manually place a few bar markers or do a quick GUI mapping in Logic/Reaper to lock down downbeats.
- Ableton import expectations: Import `tempo.mid` into Arrangement to view/edit the tempo envelope. Session Scenes won’t follow a changing envelope; for live reliability, keep timing authoritative in audio (printed click/cues) and run Warp Off.

Next steps
- Drop `14_Cues.wav` into each song’s `Stems` and continue with the bulk import into Ableton Session.

Next step: [Tracks Prep](tracks-prep.md)
