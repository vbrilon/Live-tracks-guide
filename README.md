# Live Backing Tracks with XR18 + Ableton (Mac)

Beginner-friendly guide to build a reliable live backing‑tracks rig using:
- Mixer: Behringer X Air XR18 (FOH)
- DAW: Ableton Live (Mac) with Ableset
- Prep DAW: Logic Pro for tempo mapping, click, and vocal cues
- Sample rate: 48 kHz; Buffer: 128–256 samples

## Hardware & Software Checklist
- Mac laptop with Ableton Live (latest) and Ableset installed
- Logic Pro (for tempo map + click/cues prep)
- XR18 on latest firmware; X Air Edit installed on Mac
- USB‑B cable (Mac ⇄ XR18), TRS cables to IEM transmitters/amps, power
- MIDI foot controller for the drummer (for transport control)

## File Organization
- `LiveTracks/Songs/<SongName>/Stems/` — exported WAV stems (48k/24‑bit)
- `LiveTracks/Songs/<SongName>/MIDI/` — optional tempo/marker MIDI (reference)
- `LiveTracks/Songs/<SongName>/Session/` — Ableton set(s) and Ableset data
- Naming (example): `RunAway_148BPM_Gmin_Drums.wav`, `RunAway_Click.wav`, `RunAway_Cues.wav`

## Channel Map (XR18)
- 1 Kick, 2 Snare, 3 Tom, 4 OH L, 5 OH R
- 6 Bass DI, 7 Guitar
- 8 Lead Vox, 9 BGV 1, 10 BGV 2
- 11 Talkback (IEM only), 12 Spare
- 13 Click (USB 13, Main LR OFF)
- 14 Cues (USB 14, Main LR OFF)
- 15 Tracks 1 (Perc/Loops)
- 16 Tracks 2 (Synth/Bass)
- 17 Tracks 3 (Keys/Pads)
- 18 Tracks 4 (BGV/FX)

## IEM Bus Plan (mono)
- Bus 1 Drummer, 2 Bassist, 3 Guitarist, 4 Lead Vox, 5 BGV/Spare
- Sends tap: Pre EQ (recommended so FOH EQ/faders don’t affect IEMs)
- Aux Out 1–5 feed your IEM transmitters/amps; set safe gain structure

---

## Part 1 — Prepare Songs in Logic Pro
1) Project setup
- Create new project at 48 kHz, 24‑bit; set time signature.
- Import the backing track audio (full mix or stem you’ll align to).

2) Generate a tempo map
- In the Smart Tempo button, choose Adapt. Play/locate through the song so Logic adapts to the audio.
- Open the Smart Tempo/Beat Mapping/Global Tracks and verify downbeats, tempo changes, and any time signature changes.
- Add arrangement markers (Intro, Verse, Chorus, Bridge) on the correct bars.

3) Build click and vocal cues
- Create a click track (accent bar 1). Keep it as audio or print from the metronome.
- Import or record vocal cue prompts (e.g., “2‑3‑4 Chorus”) precisely on the bar/beat grid.

4) Export assets
- File → Export → All Tracks as Audio Files
  - WAV, 24‑bit, 48 kHz, Normalize Off; export stems (Drums, Bass, Keys, FX, Click, Cues, etc.).
- Optional: File → Export → Tempo/Signature (MIDI) for reference. Note: Ableton does not reliably import tempo from MIDI; the audio click/cues will be your timing reference in Live.
- Save into `LiveTracks/Songs/<SongName>/Stems/` (and `MIDI/` if exported).

Tip: Keep stems loud enough but leave headroom (peaks around −6 dBFS).

## Part 2 — Create the Ableton Session (Session View)
1) Audio preferences
- Preferences → Audio: Device `X‑AIR XR18` (CoreAudio), Sample rate 48 kHz, Buffer 128–256.
- Output Config: enable at least Mono 1–18.
- Record/Warp/Launch: disable Auto‑Warp Long Samples (you’ll use unwarped stems).

2) Tracks and routing
- Create audio tracks: `Click`, `Cues`, `Tracks 1`, `Tracks 2`, `Tracks 3`, `Tracks 4`.
- Set `Audio To` for each:
  - Click → `Ext. Out 13`
  - Cues → `Ext. Out 14`
  - Tracks 1 → `Ext. Out 15`
  - Tracks 2 → `Ext. Out 16`
  - Tracks 3 → `Ext. Out 17`
  - Tracks 4 → `Ext. Out 18`

3) Import stems per song
- For each song folder, drag stems into a new Scene (one row per song).
- For each clip: open Clip View and turn Warp Off. Set clip Gain to balance. Color code per song.
- Keep click/cues as audio clips; do not use Live’s metronome for tempo‑changing songs.

4) Organize for Ableset
- Name scenes with order numbers (e.g., `01 Run Away`, `02 Skyline`).
- Group related tracks (optional) and set Stop buttons for empty clip slots.
- Save the set in `LiveTracks/Songs/<SongName>/Session/` or keep a master set for multiple songs.

## Part 3 — Ableset (Setlist & Control)
- Open Ableset; connect to Ableton. It will read Scenes as songs.
- Build your setlist, define song sections if desired, and enable transport.
- MIDI foot controller: in Ableset Preferences → MIDI, add device and map Play/Stop/Next/Prev to your footswitch.
- Test: fire a few songs; ensure the correct clips launch and stop cleanly.

## Part 4 — XR18 Routing (X Air Edit on Mac)
1) Global
- Setup → Audio/MIDI: Sample Rate 48 kHz. Confirm USB interface recognized by macOS.

2) Channel sources
- On channels 13–18, set Source to `USB` (Card). On 1–12, keep `Analog`.
- On ch 13 (Click) and 14 (Cues): disable `Main LR` send.
- On ch 15–18 (stems): enable `Main LR` and set initial faders around −10 dB.

3) IEM sends
- Buses 1–5: set Send Tap to `Pre EQ` (Bus Sends → Gear icon or per‑channel send tap).
- Build mixes per performer by raising sends from each needed channel.
- Talkback mic: assign to a spare input (e.g., ch 11) with `Main LR` off; send to IEM buses as needed.

4) Outputs
- Aux Out 1–5 → bus 1–5 (default). Connect to IEM transmitters/amps. Set transmitter inputs to line level.
- Save an XR18 Scene (e.g., `XR18_LiveTracks_Base.scn`).

## Part 5 — Soundcheck & Operation
- Power up order: XR18 → Mac/USB → Launch Ableton/Ableset → Load set.
- Line check: confirm all live mics/instruments (1–12).
- Tracks check: play a song; verify:
  - Click only in IEMs (no Main LR on ch 13)
  - Cues only in IEMs (no Main LR on ch 14)
  - Stems audible in FOH and in IEM mixes
- Gain staging: target nominal around 0 dB on channel meters; avoid red.
- Virtual soundcheck: with band muted, play stems to set FOH/IEM balances safely.

## Troubleshooting
- No XR18 as device in Ableton: check USB cable/port; power‑cycle XR18; reboot Ableton.
- No audio on ch 13–18: verify Ableton `Audio To` Ext. Out mapping and XR18 channel Source = USB.
- Click/Cues in mains: confirm `Main LR` is OFF on ch 13–14.
- Latency/pops: increase buffer to 256; close background apps; use wired Ethernet/Wi‑Fi off if using OSC.
- Clips out of sync: ensure Warp is Off on all stems; re‑export aligned stems from Logic.
- Ableset not controlling: verify MIDI device enabled in Ableset; Live is in focus; check mappings.

## Quick Reference
- Sample rate: 48 kHz; Buffer: 128–256
- Ableton outputs: Click 13, Cues 14, Stems 15–18 → XR18 ch 13–18 (USB)
- IEM buses: 1–5 mono, Pre EQ; Aux Out 1–5 → IEM chain
- Safety: `Main LR` OFF on Click/Cues; keep talkback to IEM only

---

This workflow keeps timing authoritative in audio (click/cues), avoids MIDI tempo import pitfalls, and gives FOH control over key stems while isolating click/cues to the band’s IEM mixes.

