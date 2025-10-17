[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# How To Prepare Tracks For Live Use

File organization and naming
- `LiveTracks/Songs/<SongName>/Stems/` — WAV stems (48 kHz / 24‑bit)
- `LiveTracks/Songs/<SongName>/MIDI/` — optional tempo/marker MIDI (reference only)
- `LiveTracks/Songs/<SongName>/Session/` — Ableton set(s) + Ableset data
- Naming examples (fast import by channel index):
  - Core: `13_Click.wav`, `14_Cues.wav`, `15_TracksA.wav`, `16_TracksB.wav`, `17_TracksC.wav`, `18_TracksD.wav`
  - Optional dedicates: `06_Bass.wav`, `07_Guitar.wav`, `12_Keys.wav`, `08_LeadVox.wav`
  - Drums multi‑stem: `01_Kick.wav`, `02_Snare.wav`, `03_Tom.wav`, `04_OH_L.wav`, `05_OH_R.wav`
  - Drums stereo fallback: `04_Drums_L.wav`, `05_Drums_R.wav`

Critical rule — channel numbers never change
- For any instrument: keep the same channel number whether it’s live or from tracks. Route Ableton to the live channel’s number and flip the XR18 channel Source (Analog ↔ USB).
- Examples: Bass → ch 6, Guitar → ch 7, Keys → ch 12. If running drum tracks, route Kick/Snare/Tom/OH to ch 1–5 and remove drums from stems feeding 15–18.
- Avoid duplication: when you promote an instrument to a dedicated channel, remove it from the stems so it isn’t doubled in FOH or IEMs.

## Logic Work (tempo map, click, cues, export)
1) Project setup
- New project at 48 kHz, 24‑bit; set correct time signature.
- Import the song’s reference audio (full mix or a stem).

2) Generate a tempo map
- Smart Tempo: choose Adapt; play/locate so Logic adapts to the audio.
- Verify downbeats/tempo/time‑signature in Global Tracks; fix misalignments.
- Add arrangement markers (Intro/Verse/Chorus/Bridge) on bar lines.

3) Build click and vocal cues
- Create a click track (accent bar 1). You can print it as audio.
- Import or record vocal cues (e.g., “2‑3‑4 Chorus”) aligned to the grid.

4) Export stems
- File → Export → All Tracks as Audio Files
  - WAV, 24‑bit, 48 kHz, Normalize Off.
- Optional: File → Export → Tempo/Signature (MIDI) as reference. Ableton often ignores MIDI tempo—use audio click/cues for timing in Live.
- Save into the `Stems/` folder; keep peaks around −6 dBFS for headroom.

Screenshots that help here
- Smart Tempo/Beat Mapping showing downbeats aligned.

  ![Logic Pro — Smart Tempo / Global Tracks](../Assets/img/screenshots/logic-smart-tempo.png)

  Note: TODO — replace with your own screenshot (Global Tracks visible with downbeats aligned).

- Export dialog with 48 kHz / 24‑bit / Normalize Off.

  ![Logic Pro — Export All Tracks as Audio Files](../Assets/img/screenshots/logic-export-all-tracks.png)

  Note: TODO — replace with your own screenshot of the Export dialog.

## Ableton Work (routing, scenes, warp)
1) Audio preferences
- Preferences → Audio: Audio Device `X‑AIR XR18 (CoreAudio)`, 48 kHz, Buffer 128–256.
- Output Config: enable Mono 1–18.
- Record/Warp/Launch: disable “Auto‑Warp Long Samples”.

2) Create tracks and route outputs
- Create audio tracks: `Click`, `Cues`, `Tracks 1`, `Tracks 2`, `Tracks 3`, `Tracks 4`.
- Set `Audio To`:
  - Click → `Ext. Out 13`
  - Cues → `Ext. Out 14`
  - Tracks 1 → `Ext. Out 15`
  - Tracks 2 → `Ext. Out 16`
  - Tracks 3 → `Ext. Out 17`
  - Tracks 4 → `Ext. Out 18`
- Instrument‑swappable parts: add dedicated `Bass` → `Ext. Out 6`, `Guitar` → `Ext. Out 7`, `Keys` → `Ext. Out 12` as needed. When you promote a part to a dedicated channel, remove that instrument from the stems (e.g., if using `Keys` on 12, do not include Keys inside the stem on 17).
- No live drummer: add `Kick` → 1, `Snare` → 2, `Tom` → 3, `OH L` → 4, `OH R` → 5 (or `Drums L` → 4, `Drums R` → 5 if stereo).

3) Import stems per song
- Drag each song’s stems into a new Scene (one row per song).
- For every clip: turn Warp Off, set clip Gain for balance, color code.
- Keep click/cues as audio clips; don’t rely on Live’s metronome for tempo‑changing songs.

4) Organize for Ableset
- Name scenes with order numbers: `01 Run Away`, `02 Skyline`.
- Optionally group tracks and stop empty clip slots.
- Save the set in `Session/` or maintain one master set covering many songs.

Screenshots that help here
- Output Config window with Mono 1–18 enabled.

  ![Ableton Live — Output Config (Mono 1–18 enabled)](../Assets/img/screenshots/ableton-prefs-output-config.png)

  Note: TODO — replace with your own screenshot captured on your system (Preferences → Audio → Output Config).

- Track I/O section showing `Audio To: Ext. Out 13–18`.

  ![Ableton Live — Track I/O routing to Ext. Out 13–18](../Assets/img/screenshots/ableton-track-io-ext-out-13-18.png)

  Note: TODO — replace with your own screenshot (toggle I/O section with the I/O button in Session View).

- Clip View with Warp Off.

  ![Ableton Live — Clip View with Warp Off](../Assets/img/screenshots/ableton-clip-warp-off.png)

  Note: TODO — replace with your own screenshot showing the Warp switch disabled for a stem.

## Ableset Work (setlist and control)
- Open Ableset and connect to Ableton; it reads Scenes as songs.
- Build a setlist, define sections, and enable transport control.
- Map a MIDI foot controller: Preferences → MIDI → add device → map Play/Stop/Next/Prev.
- Test navigating songs and stopping cleanly.

Screenshots that help here
- Ableset setlist view and MIDI mapping screen.

  ![Ableset — Setlist preview (vendor image)](https://ableset.app/static/social-card-c0638640604c95617d06bf2323e02cc4.jpg)

  Note: Temporary vendor image for visual context.
  TODO — add and use your own screenshots instead:
  - `../Assets/img/screenshots/ableset-setlist.png`
  - `../Assets/img/screenshots/ableset-midi-mapping.png`

[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)
