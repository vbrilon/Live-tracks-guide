# LiveTracks Guide — Project Overview

This file captures all critical context, decisions, and how‑tos so you can resume work without prior memory.

## Purpose
A beginner‑friendly, reliable workflow to run live backing tracks from a Mac into a Behringer X Air XR18 using Ableton Live + Ableset, with optional P16‑M Ultranet personal mixers. The guide includes automation to convert per‑song MP3 folders into standard stems, generate tempo maps from click audio, and assemble a multi‑song Ableton set.

## Core Conventions
- Audio settings: 48 kHz; Buffer 128–256 samples.
- Ableton outputs (Session View):
  - Click → Ext. Out 13 (XR18 ch 13), Main LR OFF
  - Cues → Ext. Out 14 (XR18 ch 14), Main LR OFF
  - Stems (four groups) → Ext. Out 15–18 (XR18 ch 15–18)
- Channel consistency (must do): For ANY instrument swapped live ↔ tracks, keep the same XR18 channel number. Only flip channel Source (Analog ↔ USB) and route Ableton to that exact number. Remove that instrument from stems to avoid doubles.
- Drums mapping:
  - Live drummer: Kick 1, Snare 2, Tom 3, OH L 4, OH R 5
  - No drummer (tracks): Mono drums on ch 4; or stereo on 4/5; or multi‑stem 1–5
- Break music (between sets): macOS system audio → USB 1/2
  - Create two XR18 Scenes:
    - Performance: ch 17/18 Source = USB 17/18 (stems)
    - Break Music: ch 17/18 Source = USB 1/2 (Mac apps)
  - In Break Scene, set ch 1/2 Source = Analog (or mute) so USB 1/2 only feeds ch 17/18.
- IEM buses: Use Pre‑EQ taps for Buses 1–5. Consider a gentle limiter/comp on each IEM bus.
- P16/Ulnet: 16 mono slots. Recommended map includes live channels, Click 11, Cues 12, Stems A–D on 13–16. You can feed a “Drums” submix to one Ultranet slot via a spare bus.

## Repo Structure (docs)
- `README.md` — Master index. Quick reference + links.
- `docs/getting-started.md` — First‑time setup for Ableton + Ableset; MIDI Out track workflow.
- `docs/architecture.md` — Concepts, device flow, prep DAW choices (Logic/Ableton/Reaper).
- `docs/xair-routing.md` — XR18 channel map, Sources, IEMs, safety, Break Music Scenes.
- `docs/ultranet-routing.md` — P16 mapping, bus submix (Drums) to save slots.
- `docs/tracks-prep.md` — File org, Logic prep (why/when), Ableton tracks/routing, Ableset.
- `docs/reaper-batch-prep.md` — Large‑catalog prep via Reaper + SWS (batch render).
- `docs/automation-bulk-import.md` — MP3 folders → WAV stems → fast Ableton import.
- `docs/tempo-map-from-click.md` — Auto‑build tempo.mid from click audio (aubio/CLI) or Reaper.
- `docs/operation.md` — Power‑up, soundcheck, show ops, quick reference.
- `docs/troubleshooting.md` — Common issues + fixes.

## Tools (automation)
- `tools/build_stems.py`
  - Input: `~/Dropbox/Song_Tracks/<SongName>/*.mp3` (per‑instrument + click)
  - Output: `LiveTracks/Songs/<SongName>/Stems/`
    - `13_Click.wav` (from click mp3)
    - `14_Cues.wav` (if cues mp3 exists)
    - `15_TracksA.wav`, `16_TracksB.wav`, `17_TracksC.wav`, `18_TracksD.wav`
  - Usage:
    - Dry‑run: `python3 tools/build_stems.py --root "~/Dropbox/Song_Tracks" --out "./LiveTracks/Songs" --map tools/keywords.yml --dry-run`
    - Render: `python3 tools/build_stems.py --root "~/Dropbox/Song_Tracks" --out "./LiveTracks/Songs" --map tools/keywords.yml`
  - Requires: `ffmpeg`
- `tools/keywords.yml` — Tweakable filename→group mapping (A/B/C/D, click, cues).
- `tools/click_to_tempo.py`
  - Builds `tempo.mid` from click audio using aubio beat detection (bar‑aligned grid).
  - Usage: `python3 tools/click_to_tempo.py --songs ./LiveTracks/Songs --meter 4/4`
  - Requires: `ffmpeg`, `aubio`, `mido` (Python)
- `tools/build_cues.py` + `tools/cues-template.yml`
  - Optional macOS TTS to synthesize `14_Cues.wav` from `cues.yml` (time‑stamped text).
  - Usage: `python3 tools/build_cues.py --songs ./LiveTracks/Songs`
  - Recommended for quick cues; for bar‑exact “3‑2‑1” use DAW on a tempo map.

## End‑to‑End Workflows

1) Fast import from MP3 folders → Ableton Scenes
- Run stems builder: convert each song’s mp3s into standard WAV stems at 48k/24‑bit.
- In Ableton: create tracks `Click/Cues/Tracks 1–4` routed to `Ext. Out 13–18`; disable Auto‑Warp.
- Add `LiveTracks/Songs` to Browser. For each song’s `Stems/`, select `13_..`→`18_..` and press Enter into the next Scene. Rename Scene `01 <Song>`.
- Ableset will read Scenes as songs; map foot controller; iPad remote via Ableset web UI.

2) Bar‑aligned cues/MIDI from click (no Logic required)
- Generate tempo map from click: `python3 tools/click_to_tempo.py --songs ./LiveTracks/Songs --meter 4/4` → `tempo.mid` per song.
- In DAW (Ableton Arrangement or Reaper): import `tempo.mid` to align the grid to click.
- Author cues (14_Cues) and any per‑song MIDI on the grid; export `14_Cues.wav` at 48k/24bit and (optionally) `<SongName>.mid`.
- In Ableton Session (show rig): add a `MIDI Out` track to IAC/hardware; place `<SongName>.mid` clips in the same Scene row as audio; keep Global Quantization at 1 Bar.
- Playback remains Warp Off; Live’s grid was only for authoring.

3) Logic or Reaper tempo‑map (manual GUI option)
- Logic: Smart Tempo → Adapt; add arrangement markers; record or snap cues on the bar grid; export `14_Cues.wav` (and optional tempo MIDI).
- Reaper + SWS: Detect beats from click (stretch markers) → SWS action to convert markers to tempo; export `tempo.mid` and batch‑render cues/stems via Region Render Matrix.

## Screenshots & Assets
- Capture and drop into `Assets/img/screenshots/` with these filenames:
  - X Air Edit: `xair-setup-audio-48k.png`, `xair-channel-13-mainlr-off.png`, `xair-channel-15-usb.png`, `xair-buses-pre-eq-tap.png`, `xair-routing-ultranet-grid.png`
  - Ableton: `ableton-prefs-output-config.png`, `ableton-track-io-ext-out-13-18.png`, `ableton-clip-warp-off.png`, `ableton-multi-scenes.png`, `ableton-session-scenes.png`, `ableton-midi-ports.png`
  - Ableset: `ableset-setlist.png`, `ableset-remote-url.png`, `ableset-midi-mapping.png`
  - Logic: `logic-smart-tempo.png`, `logic-export-all-tracks.png`
  - macOS: `macos-iac.png`
- One vendor image included: `Assets/img/screenshots/ableset-setlist.jpg` (temporary; replace with your own later).

## Safety & Ops Checklist
- Click/Cues (13/14): Main LR OFF always.
- Scenes: Performance vs Break Music (USB 17/18 vs USB 1/2 to ch 17/18); ch 1/2 set to Analog/muted during break.
- IEM taps: Pre‑EQ; consider bus limiter. Verify comfortable click levels.
- Global Quantization: 1 Bar in Ableton.
- Warp: OFF on all stems/click/cues.
- Mac reliability: disable sleep/screensaver/auto‑updates/notifications; wired network; backup USB cable.

## Open TODOs / Next Steps
- Add analog IEM bus diagram and XR18 routing screenshots into docs.
- Provide XR18 Scene templates (`Performance`, `Break Music`) and an Ableton .als template pre‑routed (06/07/12/13–18).
- Add pink‑noise asset (`Assets/audio/pink-noise-18dBFS.wav`) and a gain‑staging mini‑guide.
- Reaper starter: `.RPP` template with tracks (13_Click, 14_Cues, 15–18), Region Render Matrix presets, SWS action list.
- Optional: Keyboard Maestro macro to automate Ableton Scene import loop.

## Dependencies (install)
- Homebrew (macOS): `brew install ffmpeg aubio`
- Python packages: `pip install mido pyyaml`
- Apps: Ableton Live, Ableset, X Air Edit (XR18), Logic Pro (optional), Reaper + SWS (optional).

## Quick Links
- Master index: `README.md`
- Bulk import: `docs/automation-bulk-import.md`
- Tempo from click: `docs/tempo-map-from-click.md`
- Reaper batch: `docs/reaper-batch-prep.md`
- Getting started: `docs/getting-started.md`
- XR18 routing: `docs/xair-routing.md`
- Ultranet: `docs/ultranet-routing.md`
- Tracks prep: `docs/tracks-prep.md`
- Operation: `docs/operation.md`
- Troubleshooting: `docs/troubleshooting.md`

## Git Remote
- Origin: GitHub `git@github.com:vbrilon/Live-tracks-guide.git`
- Default branch: `main`

