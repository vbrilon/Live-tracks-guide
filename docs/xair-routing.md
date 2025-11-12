[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# X Air Routing (XR18)

Summary: Recommended XR18 channel map, safe Source settings, IEM sends, and “Break Music” Scenes that flip USB 1/2 to ch 17/18 between sets.

Versioning note
- Keep XR18 firmware and X Air Edit up to date. Scenes saved on newer firmware may not import on significantly older versions. Export and version your Scenes in `Assets/templates/` so you can re‑load known‑good states.

Recommended channel map
- 1 Kick, 2 Snare, 3 Tom, 4 OH L, 5 OH R
- 6 Bass DI, 7 Guitar
- 8 Lead Vox, 9 BGV 1, 10 BGV 2
- 11 Spare/Utility, 12 Keys (optional)
- 13 Click (USB 13, Main LR OFF)
- 14 Cues (USB 14, Main LR OFF)
- 15 Tracks 1 (Perc/Loops)
- 16 Tracks 2 (Synth/Bass)
- 17 Tracks 3 (Pads/FX)
- 18 Tracks 4 (BGV/FX)

Consistency rules (live ↔ tracks)
- For any instrument, the channel number stays the same whether it’s live or from tracks. You only flip the XR18 channel Source (Analog ↔ USB) and route Ableton to that exact channel number.
- Examples: Bass → ch 6, Guitar → ch 7, Keys → ch 12, Drums → ch 1–5 (if running drum tracks, route Kick/Snare/Tom/OH to 1–5 and remove drums from stems on 15–18).
- Avoid duplication: when you promote any instrument to its dedicated channel, remove it from the stems so it isn’t doubled (e.g., if Keys are on ch 12, do not include Keys inside the stem feeding ch 17).

Drum tracks variants (no live drummer)
- Preferred mono: route a single summed Drum track to ch 4 (USB Card 4). Park/mute ch 1, 2, 3, and 5.
- Stereo option: route `Drums L` → ch 4 and `Drums R` → ch 5. Park/mute ch 1–3.
- Multi‑stem option: if you exported Kick/Snare/Tom/OH, route them to ch 1–5 respectively (keep Keys/other stems out of 15–18 accordingly).

Break music via Mac (USB 1/2 → ch 17/18)
- Goal: play Spotify/Apple Music/YouTube from the Mac over the PA between sets using the existing USB cable.
- How it works: macOS sends system audio on USB channels 1/2. Temporarily map XR18 ch 17/18 Source to USB (Card 1/2) so your PA receives the Mac audio on the same stereo faders you already use.
- Steps (create two Scenes for fast switching):
  - Performance Scene (default for tracks): ch 17 Source = USB (Card 17), ch 18 Source = USB (Card 18).
  - Break Music Scene: ch 17 Source = USB (Card 1), ch 18 Source = USB (Card 2).
  - Store both Scenes. Before a break, load Break Music Scene; after the break, load Performance Scene.
- Notes
  - Keep ch 13/14 (Click/Cues) out of Main LR at all times.
  - In the Break Music Scene, set ch 1/2 Source = Analog (or mute 1/2) so USB 1/2 does not also appear on ch 1/2. This avoids duplicating the Mac audio on four faders.
  - If you plan to use break music regularly, prefer the drums‑on‑4 (mono) or 4/5 (stereo) options when there’s no live drummer. If you must use multi‑stem drums on 1–5, ensure the Break Music Scene flips ch 1/2 to Analog or mutes them during breaks.
  - Make sure Ableton stems on 17/18 are stopped/muted while Break Music Scene is loaded (to avoid mixing with system audio).
  - Alternative: use analog Line In 17/18 with a 3.5 mm → dual 1/4" TRS cable if you prefer not to remap USB.

## Buses 101 (Aux Mixes on XR18)

Concept
- A Bus is an independent mix separate from Main LR. On XR18, Buses 1–6 are typically used for IEM/wedge mixes, submixes (e.g., "Drums"), a stream/broadcast mix, or feeding personal mixers (via Ultranet) with a single blended source.
- Every channel has a send level to each Bus. You decide how much of each channel goes to a Bus, and the “tap point” determines whether FOH fader/EQ changes affect that Bus.

Tap points (per‑send)
- Pre‑EQ: the send happens before EQ, comp, and fader. Best for IEMs so FOH tweaks don’t surprise players.
- Pre‑Fader: after EQ/dynamics, before fader. Useful if you want FOH tone to carry to IEMs but not fader rides.
- Post‑Fader: follows FOH fader/EQ/dynamics. Common for FX sends or a broadcast mix that should follow FOH moves.

Typical uses
- IEM mixes: one Bus per musician (mono). Link adjacent Buses for stereo IEM (e.g., link Bus 1–2, 3–4). Keep sends Pre‑EQ for stability.
- Personal mixers (P16): save Ultranet slots by feeding a Bus submix (e.g., a “Drums” Bus) to one Ultranet slot. See Ultranet Routing.
- Click/Cues control: Keep ch 13/14 out of Main LR, but send them to IEM Buses so performers hear them.
- Stream/broadcast: dedicate a Bus for a separate mix, often with light bus compression and Post‑Fader taps to follow FOH.
- Effects: XR18 has internal FX with their own sends/returns; for simple use keep FX sends Post‑Fader so FX follow FOH levels.

Ultranet vs Buses for IEMs
- If you use P16‑M personal mixers over Ultranet, those musicians do NOT need separate IEM Buses on the XR18. Their IEMs plug into the P16‑M headphone amp (or the P16‑M line out can feed a wireless IEM transmitter).
- Mixed rigs are common: some players on P16 (Ultranet, no Bus), others on analog IEMs/wedges (use Bus 1–5 via Aux Outs).
- You can still use a Bus to create a submix that feeds one Ultranet slot (e.g., a single “Drums” slot) to save Ultranet channels.

Setup in X Air Edit (mixing a Bus)
1) Name and link (if stereo)
- On the Bus master, name it (e.g., “IEM Drummer”). To create a stereo IEM, link a pair (1↔2, 3↔4, or 5↔6) and pan channels per musician preference.
2) Choose tap
- In the Bus Sends options, set the send tap to Pre‑EQ for IEMs.
3) Mix with “Sends on Faders”
- Press Sends‑on‑Faders for the target Bus. Now the channel faders represent that Bus’s send levels—mix the performer’s balance here.
4) Route outputs
- Routing → Aux Out: map Aux Out 1–6 to Bus 1–6 respectively (default). Connect Aux Out jacks to IEM transmitters/amps.
5) Add protection
- On each IEM Bus, consider a gentle compressor/limiter to catch peaks. Keep thresholds conservative.
6) Save
- Store a Scene once your Buses are dialed.

Example layout
- Bus 1: Drummer IEM (mono)
- Bus 2: Bass IEM (mono)
- Bus 3: Guitar IEM (mono)
- Bus 4: Lead Vox IEM (mono)
- Bus 5: Keys IEM (mono)
- Bus 6: “Drums” submix to Ultranet slot 4 (saves P16 slots)

How this ties to the rest of the guide
- Tracks output: Ableton feeds ch 13–18; your IEM Buses choose how much of each to include. Click/Cues (13/14) have Main LR OFF but should be present in IEM Buses as needed.
- Ultranet: You can feed Ultranet slots directly from channels or from a Bus (e.g., a “Drums” Bus). See [Ultranet Routing](ultranet-routing.md).
- Operation: During soundcheck, use Sends‑on‑Faders to build each musician’s Bus mix. See [Operation](operation.md).

Walkthrough (PC) — Create a mono IEM Bus
- Connect X Air Edit (Windows) to the XR18.
- Select Bus 1 (Bus master strip), click its name, and rename (e.g., “IEM Drummer”).
- On any input channel, open the Sends tab; ensure the Bus 1 send tap is Pre‑EQ. Repeat for channels you’ll include in the IEM mix.
- Press “Sends on Faders” and select Bus 1. Use the channel faders to build the drummer’s mix (raise Click 13, Cues 14, vocal/instrument channels as needed).
- Routing → Aux Out: confirm Aux Out 1 = Bus 1. Physically connect Aux Out 1 to the drummer’s IEM transmitter/amp.
- Optional safety: on Bus 1, enable light compression (bus Dynamics) or insert a limiter FX.
- Store a Scene.

Walkthrough (PC) — Create a stereo IEM Bus
- Link Bus 1–2 as a stereo pair (select Bus 1, enable Link). Rename (e.g., “IEM Guitar (Stereo)”).
- Press “Sends on Faders” for Bus 1/2; pan each channel’s send for the musician’s preference.
- Routing → Aux Out: map Aux Out 1 = Bus 1 and Aux Out 2 = Bus 2; connect both outputs to the stereo IEM chain.
- Keep sends Pre‑EQ; add gentle bus compression if desired; save Scene.

Walkthrough (PC) — Drums Bus feeding P16
- Pick Bus 6 for a “Drums” submix.
- Press “Sends on Faders” for Bus 6; raise Kick/Snare/Tom/OH sends to taste; keep tap Pre‑EQ.
- Routing → Ultranet: set a slot (e.g., Slot 4) Source = Bus 6, Tap = Pre‑EQ; label it “Drums”. Now P16 users get a single “Drums” knob while FOH keeps individual drum channels.
- Save Scene.

Step‑by‑step in X Air Edit (Mac)
1) Global
- Setup → Audio/MIDI → Sample Rate: 48 kHz.
- Confirm macOS sees the XR18 as an audio device.

2) Channel sources
- On ch 13–18, set Source = USB (Card). On ch 1–12, keep Source = Analog.
- On ch 13 (Click) and 14 (Cues): turn OFF Main LR.
- On ch 15–18 (stems): keep Main LR ON; start faders around −10 dB.
- Instrument‑swappable channels (e.g., Bass ch 6, Guitar ch 7):
  - Backing → set Source = USB (Card 6/7)
  - Live player → set Source = Analog
- No live drummer:
  - Mono summed drums → set ch 4 Source = USB (Card 4); park/mute ch 1, 2, 3, 5.
  - Stereo drums → set ch 4/5 Source = USB (Card 4/5); park/mute ch 1–3.
  - Multi‑stem drums → set ch 1–5 Source = USB (Card 1–5).

3) IEM sends
- Buses 1–5: set Send Tap = Pre‑EQ (so FOH tweaks don’t change IEMs).
- Build each performer’s mix by raising sends from the needed channels.
- Safety: consider a gentle compressor/limiter on each IEM bus (or an inserted limiter FX) to catch peaks. Set thresholds conservatively to avoid pumping.

4) Outputs
- Aux Out 1–5 → Bus 1–5 (default). Connect to IEM transmitters/amps at line level.
- Save a base Scene, e.g., XR18_LiveTracks_Base.scn.

Helpful screenshots
- Channel view: Source selector (USB vs Analog).

  ![X Air Edit — Channel Source set to USB](../Assets/img/screenshots/xair-channel-15-usb.png)

  Note: TODO — replace with your own screenshot showing ch 15 set to USB (Card 15).
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

- Ch 13–14 with Main LR OFF (Click/Cues safety).

  ![X Air Edit — Ch 13 Main LR OFF](../Assets/img/screenshots/xair-channel-13-mainlr-off.png)

  Note: TODO — replace with your own screenshot for both ch 13 and 14.
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

- Bus sends tap set to Pre‑EQ.

  ![X Air Edit — Bus Sends Tap Pre‑EQ](../Assets/img/screenshots/xair-buses-pre-eq-tap.png)

  Note: TODO — replace with your own screenshot (Bus Sends gear → Pre‑EQ).
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

- Setup → Audio/MIDI at 48 kHz.

  ![X Air Edit — Setup 48 kHz](../Assets/img/screenshots/xair-setup-audio-48k.png)

  Note: TODO — replace with your own screenshot.
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

Next step: [Ultranet Routing](ultranet-routing.md)

[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)
