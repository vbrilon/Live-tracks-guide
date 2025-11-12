[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# Getting Started (Ableton Live + Ableset)

Summary: First‑time setup for Ableton + Ableset to build a basic show, with iPad remote and optional MIDI Out track.

## Part A — Ableton Live: Your First Live Set

1) Install and launch
- Install Ableton Live on your Mac and open it.
- If prompted for audio, skip for now; set it in Preferences.

2) Configure audio
- Open Preferences → Audio.
- Audio Device: select `X‑AIR XR18 (CoreAudio)`.
- Sample Rate: 48 kHz. Buffer Size: 128–256.
- Output Config: enable Mono 1–18.

Screenshots to add
- Preferences → Audio (device, sample rate, buffer): `../Assets/img/screenshots/ableton-prefs-audio.png` (TODO add)
- Output Config with Mono 1–18 enabled: `../Assets/img/screenshots/ableton-prefs-output-config.png` (TODO add)

Windows specifics
- Install and select the official `X‑AIR ASIO` driver in Ableton (Options → Preferences → Audio).
- Device name may appear as `X‑AIR XR18 ASIO`. Enable outputs 1–18 in Output Config.
- If using WASAPI/shared drivers, latency and channel exposure can vary; prefer ASIO for stable multichannel output.

3) Prepare the set
- Record/Warp/Launch tab: disable “Auto‑Warp Long Samples”.
- In Session View (tab near top right), create these audio tracks:
  - `Click`, `Cues`, `Tracks 1`, `Tracks 2`, `Tracks 3`, `Tracks 4`.
- Set Audio To for each track:
  - Click → `Ext. Out 13`
  - Cues → `Ext. Out 14`
  - Tracks 1 → `Ext. Out 15`
  - Tracks 2 → `Ext. Out 16`
  - Tracks 3 → `Ext. Out 17`
  - Tracks 4 → `Ext. Out 18`
- Optional dedicated tracks for missing players: `Bass` → `Ext. Out 6`, `Guitar` → `Ext. Out 7`, `Keys` → `Ext. Out 12`.

Screenshots to add
- Track I/O set to Ext. Out 13–18: `../Assets/img/screenshots/ableton-track-io-ext-out-13-18.png` (TODO add)

4) Add your first song
- File organization: put stems in `LiveTracks/Songs/<SongName>/Stems/` (48 kHz/24‑bit WAVs).
- Drag stems into one row in Session View (one Scene per song). For example:
  - Click.wav → `Click` track
  - Cues.wav → `Cues` track
  - TracksA/B/C/D.wav → `Tracks 1–4` tracks
- For each clip: open Clip View and turn Warp Off. Adjust clip Gain to taste.
- Rename the Scene: `01 <SongName>`.

Count‑in convention (recommended)
- Standardize on a 2‑bar pre‑roll: Click/Cues files contain two bars of count‑in; other stems contain two bars of silence before the music starts. This ensures every Scene launch gives the band the same lead‑in before the song hits.
- If your stems don’t include this yet, add the 2‑bar pre‑roll during prep in Logic or Reaper before exporting. See `docs/tracks-prep.md`.

5) Add more songs (multi‑song set)
- Repeat step 4 for each additional song: one Scene (row) per song using the same tracks.
- Rename Scenes with leading numbers so they sort cleanly: `02 <Song2>`, `03 <Song3>`, etc.
- Color‑code each song’s clips consistently (e.g., all clips in a song share a color) to avoid misfires during the show.
- Stop buttons: right‑click empty clip slots in your tracks and choose “Stop” (or enable Stop buttons) so launching one song’s Scene doesn’t accidentally stop another track.
- Global Quantization: set to 1 Bar (top center of Live). This ensures smooth starts/stops and transitions when launching Scenes.
- Optional: add Section markers in Ableset (Part B) rather than using Follow Actions; for tempo‑changing content keep timing authoritative in audio (click/cues), not warped automation.

Screenshots to add
- Clip View with Warp Off: `../Assets/img/screenshots/ableton-clip-warp-off.png` (TODO add)
- Session View with scenes labeled: `../Assets/img/screenshots/ableton-session-scenes.png` (TODO add)

5) Save
- Save the set to `LiveTracks/Songs/<SongName>/Session/YourBand_Live.als`.

6) Test audio
- Play the Scene. On XR18 (X Air Edit), confirm ch 13–18 are set to USB.
- Ensure `Main LR` is OFF on ch 13 (Click) and 14 (Cues). You should only hear click/cues in IEMs, and stems in FOH/IEMs.

Tips
- Color‑code each song’s clips; keep a consistent color legend.
- Use “Stop” buttons to prevent empty slots from stopping other clips.

Session vs Arrangement (what to use here)
- This workflow uses Session View (grid) to trigger songs as Scenes. Arrangement View is great for linear editing, but for live playback Session View is simpler and safer.

Screenshots to add
- Session View with multiple songs (Scenes) and Global Quantization visible: `../Assets/img/screenshots/ableton-multi-scenes.png` (TODO add)

## Optional — Add a MIDI Out Track (testing / program changes)

Goal: Play a per‑song MIDI clip alongside the audio to test lights, keys changes, program changes, or outboard.

1) Enable a virtual MIDI port (macOS)
- Open `Audio MIDI Setup` → `Window` → `Show MIDI Studio`.
- Double‑click `IAC Driver` → check `Device is online` → apply.

2) Ableton MIDI prefs
- Preferences → Link/MIDI: under `MIDI Ports`, enable `Track` and `Remote` for `IAC Driver (Bus 1)` Output.

3) Create a `MIDI Out` track
- Add a MIDI track named `MIDI Out`.
- Set `MIDI To` → `IAC Driver (Bus 1)` → Channel as needed (e.g., 1). For hardware, choose your external MIDI interface instead.

4) Per‑song MIDI clip
- For each song, drag its MIDI file (e.g., `<SongName>.mid`) into the `MIDI Out` clip slot in the same Scene row as the audio.
- Set Global Quantization to 1 Bar so the MIDI and audio start together when the Scene is launched.

Notes
- Variable‑tempo songs: Session Scenes don’t carry a tempo envelope (one BPM per Scene only). If your MIDI must follow a changing tempo (e.g., arps), author/export that part to audio or run the song from Arrangement (with a Master tempo envelope). Program changes and one‑shots are typically fine in Session.
- For synth testing: add an `External Instrument` device on the `MIDI Out` track to monitor return audio if desired.

Screenshots to add
- IAC Driver enabled: `../Assets/img/screenshots/macos-iac.png` (TODO add)
- Ableton MIDI Ports (IAC Output Track/Remote ON): `../Assets/img/screenshots/ableton-midi-ports.png` (TODO add)

## Part B — Ableset: Setlist + Remote Control (iPad)

1) Install and connect
- Install Ableset on your Mac and open it while Ableton is running.
- Ableset will read Ableton Scenes as songs.

2) Build your setlist
- In Ableset, add/reorder songs as needed.
- Optional: define song sections (Intro/Verse/Chorus) to jump within a song.

3) Map a MIDI foot controller (optional)
- Ableset → Preferences → MIDI → add your device → map Play/Stop/Next/Prev.

4) Control from an iPad (web browser)
- Ensure the Mac and the iPad are on the same local network. For reliability, use your own dual‑band router; avoid crowded venue Wi‑Fi.
- In Ableset, open the Remote/Web interface. Ableset will show a local URL (e.g., `http://<your-mac-ip>:<port>`).
- On the iPad, open Safari and enter that URL to control songs and transport.
- Optional iPad tweaks: disable Auto‑Lock during shows; add the page to Home Screen for full‑screen control; consider Guided Access to lock the device to the control page.

Troubleshooting iPad control
- If the page doesn’t load: confirm both devices are on the same network, try the Mac’s Wi‑Fi IP (System Settings → Network), and temporarily allow Ableset connections through macOS firewall if prompted.
- If Ableset doesn’t control Ableton: ensure Ableton is running, the set is open, and Ableset shows a connected state.

Screenshots to add
- Ableset setlist view: `../Assets/img/screenshots/ableset-setlist.png` (TODO add)
- Ableset remote URL display: `../Assets/img/screenshots/ableset-remote-url.png` (TODO add)
- Ableset MIDI mapping: `../Assets/img/screenshots/ableset-midi-mapping.png` (TODO add)

## Part C — Common Workflow Examples

1) No live bassist
- Route `Bass` track to `Ext. Out 6` in Ableton.
- On XR18, flip ch 6 Source to USB (Card 6). When a bassist returns, flip Source back to Analog. Channel numbers stay the same.

2) No live drummer
- Mono drums: route a summed `Drums` track to `Ext. Out 4`; on XR18 set ch 4 Source = USB (Card 4). Park/mute ch 1/2/3/5.
- Stereo drums: route `Drums L` → `Ext. Out 4`, `Drums R` → `Ext. Out 5`; set ch 4/5 Source = USB (Card 4/5).
- Multi‑stem drums: route Kick/Snare/Tom/OH to `Ext. Out 1–5` and flip XR18 1–5 to USB.

3) Between‑set music (Mac → PA)
- Create two XR18 Scenes:
  - Performance: ch 17/18 Source = USB 17/18
  - Break Music: ch 17/18 Source = USB 1/2, ch 1/2 Source = Analog (or muted)
- Set Mac output device to XR18; play Spotify/Apple Music; control level on ch 17/18.

4) Click‑only rehearsal
- Launch only Click/Cues Scenes; mute/stop Tracks 1–4.
- Verify `Main LR` OFF on ch 13/14 so click/cues stay out of mains.

5) Promote Keys to a dedicated channel
- Add a `Keys` track in Ableton → `Ext. Out 12`.
- Remove Keys from any stems feeding ch 17; on XR18 set ch 12 Source = USB (Card 12).
- When a keys player returns, flip ch 12 Source back to Analog.

6) Emergency 2‑track backup
- Keep a stereo mixdown of each song routed to `Ext. Out 17/18`.
- If stems fail, mute Tracks 1–4 and fire the stereo mix clips on 17/18.

Next step: [Tracks Prep](tracks-prep.md)

[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)
