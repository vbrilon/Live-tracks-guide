[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# Getting Started (Ableton Live + Ableset)

This guide assumes no prior experience with Ableton Live or Ableset. It walks you from an empty project to a basic show you can control from an iPad.

## Part A — Ableton Live: Your First Live Set

1) Install and launch
- Install Ableton Live on your Mac and open it.
- If prompted for audio, skip for now; we’ll set it in Preferences.

2) Configure audio
- Open Preferences → Audio.
- Audio Device: select `X‑AIR XR18 (CoreAudio)`.
- Sample Rate: 48 kHz. Buffer Size: 128–256.
- Output Config: enable Mono 1–18.

Screenshots to add
- Preferences → Audio (device, sample rate, buffer): `../Assets/img/screenshots/ableton-prefs-audio.png` (TODO add)
- Output Config with Mono 1–18 enabled: `../Assets/img/screenshots/ableton-prefs-output-config.png` (TODO add)

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

[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

