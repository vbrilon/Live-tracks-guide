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

## System Diagram (Ultranet P16‑M Example)
```
 [Mac Laptop]
 (Ableton Live + Ableset)
         ||  USB‑B
         \\==============================>
                                   [Behringer X Air XR18]
                                   (FOH mixer + USB interface)
           Analog Inputs 1–12   ^          |  Ultranet (RJ45)
   Mics, DI, instruments  ----->|          v
                                              [Ultranet Hub]
                                              (Behringer P16‑D or compatible)
                                                  |—> [P16‑M Drummer]
                                                  |—> [P16‑M Bassist]
                                                  |—> [P16‑M Guitar]
                                                  |—> [P16‑M Lead Vox]
                                                  |—> [P16‑M BGV]

   Main L/R  =======================>  FOH/PA
```
Notes
- Use an Ultranet distributor (e.g., P16‑D). A regular Ethernet switch will not work; Ultranet is not standard Ethernet.
- P16‑M units can also daisy‑chain; the P16‑D provides power + distribution over Ultranet.
- This setup replaces analog IEM buses; personal mixes are made on each P16‑M using up to 16 Ultranet channels.

## Ultranet Routing (XR18 → P16‑M)
Ultranet carries 16 mono channels. Assign XR18 sources to Ultranet slots so every musician can build their own mix on a P16‑M. Use Pre‑EQ (or Pre‑Fader) taps so FOH changes don’t affect IEMs.

How to assign
- In X Air Edit: Routing → Ultranet.
- For each Ultranet 1–16 slot: set Source to `DirOut Ch X` (or Card/Bus as noted) and Tap to `Pre EQ`.
- Store as a Scene once verified.

Recommended map (4 track stems)
| Ultranet | Source (XR18)     | Tap    | Purpose                   |
|----------|--------------------|--------|---------------------------|
| 1        | DirOut Ch1         | Pre EQ | Kick                      |
| 2        | DirOut Ch2         | Pre EQ | Snare                     |
| 3        | DirOut Ch3         | Pre EQ | Tom                       |
| 4        | DirOut Ch4         | Pre EQ | OH L                      |
| 5        | DirOut Ch5         | Pre EQ | OH R                      |
| 6        | DirOut Ch6         | Pre EQ | Bass (live or backing)    |
| 7        | DirOut Ch7         | Pre EQ | Guitar (live or backing)  |
| 8        | DirOut Ch8         | Pre EQ | Lead Vox                  |
| 9        | DirOut Ch9         | Pre EQ | BGV 1                     |
| 10       | DirOut Ch10        | Pre EQ | BGV 2                     |
| 11       | DirOut Ch13 (USB)  | Pre EQ | Click (IEM only)          |
| 12       | DirOut Ch14 (USB)  | Pre EQ | Cues (IEM only)           |
| 13       | DirOut Ch15 (USB)  | Pre EQ | Tracks A (Perc/Loops)     |
| 14       | DirOut Ch16 (USB)  | Pre EQ | Tracks B (Synth/Bass)     |
| 15       | DirOut Ch17 (USB)  | Pre EQ | Tracks C (Keys/Pads)      |
| 16       | DirOut Ch18 (USB)  | Pre EQ | Tracks D (BGV/FX)         |

Notes and variants
- Keep Click/Cues out of Main LR; Ultranet delivery is independent of mains.
- Talkback is not mapped in this 4‑stem layout. If needed on P16, repurpose a slot (e.g., collapse OH to mono) or feed talkback via a shared bus.
- Instrument‑swappable channels (e.g., Bass ch 6): when switching live ↔ track, the P16 feed stays on the same Ultranet slot; only the channel Source flips (Analog ↔ USB).

## File Organization
- `LiveTracks/Songs/<SongName>/Stems/` — exported WAV stems (48k/24‑bit)
- `LiveTracks/Songs/<SongName>/MIDI/` — optional tempo/marker MIDI (reference)
- `LiveTracks/Songs/<SongName>/Session/` — Ableton set(s) and Ableset data
- Naming (examples):
  - Descriptive: `RunAway_148BPM_Gmin_Drums.wav`, `RunAway_Click.wav`, `RunAway_Cues.wav`
  - Channel‑indexed (recommended for fast import): `06_Bass.wav`, `07_Guitar.wav`, `13_Click.wav`, `14_Cues.wav`, `15_TracksA.wav`, `16_TracksB.wav`, `17_TracksC.wav`, `18_TracksD.wav`

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
- Analog IEM alternative if not using P16 personal mixers.
- Bus 1 Drummer, 2 Bassist, 3 Guitarist, 4 Lead Vox, 5 BGV/Spare
- Sends tap: Pre EQ (recommended so FOH EQ/faders don’t affect IEMs)
- Aux Out 1–5 feed your IEM transmitters/amps; set safe gain structure

---

## Instrument‑Swappable Routing (Same Channel Numbers)
Goal: keep FOH/IEM processing consistent whether a part is live or on backing tracks by using the same XR18 channel number for both and switching the channel source.

### Mapping Overview
| Part   | XR18 Ch | Ableton Output | Live Source      | Backing Source   | Notes                          |
|--------|---------|----------------|------------------|------------------|---------------------------------|
| Bass   | 6       | Ext. Out 6     | Analog (DI)      | USB (Card 6)     | Same EQ/comp/sends              |
| Guitar | 7       | Ext. Out 7     | Analog (DI/Mic)  | USB (Card 7)     | Same EQ/comp/sends              |
| Click  | 13      | Ext. Out 13    | —                | USB (Card 13)    | Main LR OFF (IEM only)          |
| Cues   | 14      | Ext. Out 14    | —                | USB (Card 14)    | Main LR OFF (IEM only)          |
| Tracks 1–4 | 15–18 | Ext. Out 15–18 | —              | USB (Card 15–18) | Group stems (percussion/keys/etc.) |

### Example (Bass on channel 6)
- Live bassist: XR18 ch 6 Source = Analog; Ableton Bass track muted/disabled.
- Backing bass: Route Ableton Bass track to `Ext. Out 6`; set XR18 ch 6 Source = USB (Card 6). Keep EQ/comp/sends as usual.

### Switching Live ↔ Track (per channel)
1) Safety: Mute the channel on XR18 and lower its fader slightly to avoid pops.
2) In Ableton:
   - Live → Track: Unmute the backing clip/track; set `Audio To` to the channel’s output (e.g., Bass → `Ext. Out 6`).
   - Track → Live: Mute/stop the backing clip/track.
3) In X Air Edit (channel config):
   - Live → Track: Set `Source` to `USB (Card <ch>)` (e.g., ch 6 → Card 6).
   - Track → Live: Set `Source` to `Analog`.
4) Unmute and set level. Confirm in meters that only one source is active (no doubling).
5) Optional: Save quick scenes (e.g., `XR18_Live_Bass.scn` vs. `XR18_Track_Bass.scn`).

Apply the same pattern for any absent instrument (e.g., Guitar on ch 7 → `Ext. Out 7`). Keep Click/Cues fixed on USB 13–14 (IEM only), and use 15–18 for non‑instrument group stems.

## Channel Binding Standard (XR18 ↔ Ableton ↔ P16)
Keep indexes consistent for easy import and predictable monitoring. Channel 6 is always Bass across the system.

| Role       | XR18 Ch | Ableton Output | P16 Slot | Notes                                 |
|------------|---------|----------------|---------:|---------------------------------------|
| Kick       | 1       | Ext. Out 1     |        1 | Live mic only (backing goes to stems) |
| Snare      | 2       | Ext. Out 2     |        2 | Live mic only                         |
| Tom        | 3       | Ext. Out 3     |        3 | Live mic only                         |
| OH L       | 4       | Ext. Out 4     |        4 | Live mic only                         |
| OH R       | 5       | Ext. Out 5     |        5 | Live mic only                         |
| Bass       | 6       | Ext. Out 6     |        6 | Instrument‑swappable (live/track)     |
| Guitar     | 7       | Ext. Out 7     |        7 | Instrument‑swappable (live/track)     |
| Lead Vox   | 8       | —              |        8 | Mic input; no backing on this ch      |
| BGV 1      | 9       | —              |        9 | Mic input                             |
| BGV 2      | 10      | —              |       10 | Mic input                             |
| Click      | 13      | Ext. Out 13    |       11 | IEM only; Main LR OFF                 |
| Cues       | 14      | Ext. Out 14    |       12 | IEM only; Main LR OFF                 |
| Tracks A   | 15      | Ext. Out 15    |       13 | Perc/Loops                            |
| Tracks B   | 16      | Ext. Out 16    |       14 | Synth/Bass (no Bass if 06_Bass used)  |
| Tracks C   | 17      | Ext. Out 17    |       15 | Keys/Pads                             |
| Tracks D   | 18      | Ext. Out 18    |       16 | BGV/FX                                |

Import/backfill rules
- If using a backing Bass part, export `06_Bass.wav`, route to `Ext. Out 6`, and flip XR18 ch 6 Source to USB.
- When `06_Bass.wav` is present, remove Bass content from `16_TracksB.wav` to avoid doubling.
- If no `06_Bass.wav`, include Bass in `16_TracksB.wav` and keep XR18 ch 6 Source = Analog for a live DI (or mute if no DI connected).
- Apply the same pattern for Guitar on channel 7 as needed.

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
 - For instrument‑swappable parts (e.g., Bass when no live player): create a dedicated `Bass` track and set `Audio To` → `Ext. Out 6` (match the XR18 channel number). Do the same for any other absent instrument (e.g., Guitar → `Ext. Out 7`).

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
 - For instrument‑swappable channels (e.g., Bass on ch 6): when using backing tracks, set Source = `USB (Card 6)`; when live, set Source = `Analog`. Keep the same channel strip and sends in both cases.

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
- No bass when using backing: Ableton `Bass` track must be `Audio To: Ext. Out 6` and XR18 ch 6 Source = USB.

## Quick Reference
- Sample rate: 48 kHz; Buffer: 128–256
- Ableton outputs: Click 13, Cues 14, Stems 15–18 → XR18 ch 13–18 (USB)
- Ultranet P16: 1–10 live channels; 11 Click; 12 Cues; 13–16 four stems
- Instrument‑swappable: route backing part to the same output as the live channel number (e.g., Bass → 6) and flip XR18 channel Source (Analog ↔ USB).
- IEM buses: 1–5 mono, Pre EQ; Aux Out 1–5 → IEM chain
- Safety: `Main LR` OFF on Click/Cues; keep talkback to IEM only

---

This workflow keeps timing authoritative in audio (click/cues), avoids MIDI tempo import pitfalls, and gives FOH control over key stems while isolating click/cues to the band’s IEM mixes.

## TODO
- Add analog IEM bus variant diagram and routing steps.
- Add screenshots of X Air Edit (Ultranet routing and channel source).
- Add Ableset setlist example and MIDI footswitch mapping walkthrough.
- Add templates: Logic Pro project prep template and Ableton .als with pre-routed outputs (06 Bass, 07 Guitar, 13–18 Click/Cues/Tracks A–D).
