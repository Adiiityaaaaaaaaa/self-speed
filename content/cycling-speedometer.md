---
title: Cycling Speedometer — Track Bike Speed with GPS
description: Turn your phone into a cycling speedometer. Live speed, average, distance and max, plus GPX export to Strava or Garmin. Free, works offline, no app install.
slug: cycling-speedometer
priority: 0.9
---

# Cycling speedometer

A bike computer costs money and needs a wheel magnet, a mount and a battery you
forget to charge. Your phone already has a GPS chip that does the same job. Self
Speed turns it into a cycling speedometer in one tap — live speed, average,
distance, and a GPX file you can drop straight into Strava.

## What you get

| Reading | What it tells you |
|---|---|
| Current speed | Live km/h or mph, smoothed over 2.5 seconds |
| Max speed | Your fastest moment, usually a descent |
| Average | Moving average — stops at traffic lights don't drag it down |
| Distance | Total ridden, computed from your GPS track |
| Elapsed | Time since you pressed start |
| Accuracy | How much to trust the numbers right now |

## Why moving average matters on a bike

Most cheap speedometers give you a simple average: distance divided by total
time. Ride 20 km in an hour of pedalling plus 20 minutes waiting at junctions,
and they report 15 km/h — which tells you nothing about how you actually rode.

Self Speed excludes time spent below 0.5 m/s, so the average reflects your
riding, not your city's traffic lights. The same 20 km comes back as 20 km/h,
which is the number you actually want to compare week to week.

## GPS speed versus wheel sensors

A wheel magnet counts rotations and multiplies by a tyre circumference you typed
in once. It is precise but only as correct as that number — an under-inflated
tyre or a typo puts every ride out by a few percent, permanently.

GPS measures your actual movement across the ground. It needs no calibration and
cannot drift, but it needs sky. Under heavy tree cover or between tall buildings
the fix degrades and readings get noisy.

> In practice: GPS is more accurate on open roads, a wheel sensor is steadier in
> forests and cities. Neither is wrong; they fail in different places.

## Getting a good reading

1. **Mount the phone with a view of the sky.** In a jersey pocket it still works,
   but accuracy drops. On the bars is best.
2. **Wait for accuracy to settle.** The number in the Accuracy tile should reach
   about ±5–15 m before you set off. A cold GPS start takes 20–60 seconds.
3. **Keep the screen awake.** Self Speed requests a wake lock automatically, so
   the display stays on while tracking.
4. **Battery.** Continuous GPS is demanding. For rides over two hours, bring a
   power bank or use a dedicated computer.

## Exporting to Strava or Garmin

Press **Export GPX** after your ride and you get a standard `.gpx` file with a
timestamped point for every fix. That format is accepted by Strava, Garmin
Connect, Komoot, RideWithGPS and essentially every mapping tool.

In Strava: *Upload → File → choose your .gpx*. The ride appears with distance,
elevation and your speed curve intact.

## Limitations worth knowing

- **iOS backgrounds aggressively.** Lock the phone or switch apps and
  tracking stops. Keep Self Speed in the foreground.
- **Tunnels and underpasses** lose the fix entirely. The reading goes grey and
  resumes when you come out.
- **Elevation from GPS is poor.** Vertical accuracy is typically two to three
  times worse than horizontal. If climbing metres matter to you, use a device
  with a barometric altimeter.
