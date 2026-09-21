---
title: Running Speed and Pace Tracker — GPS Pace in Your Browser
description: Track running speed and pace with GPS in your browser. Live speed, distance, moving average and GPX export. Free, no app install, nothing uploaded.
slug: running-speed-tracker
priority: 0.9
---

# Running speed tracker

Runners think in pace — minutes per kilometre — while speedometers think in
km/h. They are the same information inverted, and converting between them in
your head mid-run is genuinely annoying. This page gives you the conversion and
a tracker that handles the rest.

## Speed to pace, converted

| Speed (km/h) | Pace (min/km) | Pace (min/mile) | Feels like |
|---|---|---|---|
| 8.0 | 7:30 | 12:04 | Easy jog |
| 10.0 | 6:00 | 9:39 | Steady run |
| 12.0 | 5:00 | 8:03 | Tempo |
| 14.0 | 4:17 | 6:54 | Threshold |
| 16.0 | 3:45 | 6:02 | 5K race pace |
| 18.0 | 3:20 | 5:22 | Fast |
| 20.0 | 3:00 | 4:49 | Elite territory |

The arithmetic: **pace in min/km = 60 ÷ speed in km/h**. A 5:00 min/km pace is
exactly 12 km/h. Marathon world record pace is roughly 21 km/h, or 2:50 min/km.

## Why GPS pace jumps around

If you have ever glanced at a running watch and seen your pace swing from 4:30
to 6:10 within a few seconds on steady effort, that is not you — it is the GPS.

A consumer GPS fix has a horizontal error of several metres. When your position
is re-estimated every second, a 3 m error in either direction translates to a
large apparent speed change over such a short interval. The error is random, so
it averages out over distance but looks dramatic instant to instant.

Self Speed smooths readings over a 2.5 second window, which removes most of the
jitter while still responding quickly when you genuinely change pace. Your total
distance stays accurate because the errors cancel over time.

## Track running is the hard case

A 400 m track is the worst possible environment for GPS pace. The bends are
tight, you are never travelling in a straight line for long, and the systematic
error of cutting or widening the corner is comparable to the lane width itself.

For track sessions, trust the track. Time your laps with a watch — 400 m is
400 m, and a stopwatch has no error budget. Use GPS for road and trail.

## Getting a usable reading

1. **Start outdoors and wait.** Let accuracy settle to ±5–10 m before you run.
   Starting inside a building and walking out gives you a bad first minute.
2. **Arm swing adds noise.** A phone in your hand moves back and forth roughly a
   metre every stride. An armband or waist belt gives cleaner data.
3. **Keep it in the foreground.** Browsers stop geolocation when the page is
   hidden, so don't switch apps mid-run.

## Exporting your run

**Export GPX** produces a standard file that Strava, Garmin Connect and every
other running platform will import directly, preserving your route and splits.

## Pace for common race targets

Working backwards from a finishing time is the most useful thing a pace table
does.

| Race | Target | Pace (min/km) | Speed (km/h) |
|---|---|---|---|
| 5K | 25:00 | 5:00 | 12.0 |
| 5K | 20:00 | 4:00 | 15.0 |
| 10K | 60:00 | 6:00 | 10.0 |
| 10K | 45:00 | 4:30 | 13.3 |
| Half marathon | 2:00:00 | 5:41 | 10.5 |
| Half marathon | 1:30:00 | 4:16 | 14.1 |
| Marathon | 4:00:00 | 5:41 | 10.5 |
| Marathon | 3:00:00 | 4:16 | 14.1 |

A useful symmetry: a half marathon in 1:30 and a marathon in 3:00 are the same
pace. Sustaining it for twice the distance is the entire difficulty.

## Why your watch and your phone disagree

Two GPS devices on the same run routinely report distances differing by 1 to 2
percent, occasionally more. Neither is broken.

- **Sampling rate.** A device recording every second captures more of a winding path than one recording every five seconds, which cuts corners and under-reads.
- **Filtering.** Each manufacturer smooths the raw track differently. Aggressive smoothing shortens distance; light smoothing inflates it with GPS noise.
- **Antenna position.** A wrist swings through roughly a metre each stride. A phone on your waist does not.

For training, consistency matters more than absolute truth. Use one device and
compare it against itself.

## Treadmills

GPS cannot measure treadmill running at all — you are not moving relative to the
ground, so your speed over ground genuinely is zero. The machine's own readout is
the only measurement available, and it is calibrated to belt speed, which drifts
as the belt wears and stretches.

## Frequently asked

### What is a good running pace?

For a recreational runner, 6:00 min/km is a comfortable steady pace and 5:00 is a
solid tempo. Context matters far more than the number — terrain, heat, humidity
and elevation all shift it substantially.

### Why does my pace look wrong at the start?

A cold GPS start takes 30 to 60 seconds to settle. Beginning your run the instant
you press go means the first minute is computed from a poor fix. Wait for the
accuracy figure to drop below about 10 m.

### Can I track a run with no signal?

Yes. GPS needs no mobile data — only a view of the sky. Load the page before you
set off and it works offline for the whole run.
