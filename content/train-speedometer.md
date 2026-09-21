---
title: Train and Transit Speedometer — How Fast Is This Train Going?
description: Find out how fast your train, bus, metro or plane is actually moving, using GPS in your browser. Free, no install, works from a window seat.
slug: train-speedometer
priority: 0.8
---

# Train and transit speedometer

How fast is this train actually going? Put your phone near the window, press
start, and find out. It works on trains, buses, ferries and — with caveats —
aircraft.

## What to expect

| Service | Typical cruising speed |
|---|---|
| City bus | 20 – 40 km/h |
| Metro / underground | 30 – 60 km/h |
| Suburban commuter rail | 60 – 100 km/h |
| Intercity express | 120 – 160 km/h |
| High-speed rail (Shinkansen, TGV, ICE) | 250 – 320 km/h |
| Commercial airliner, cruise | 800 – 950 km/h |

A note on the last row: most phone GPS chips are subject to **CoCom limits**, an
export-control restriction that disables the receiver above roughly 1,900 km/h
*and* 18,000 m altitude. Airliners sit below both thresholds, so GPS generally
works fine at cruise — the real obstacle is getting a clear view of the sky
through a small, often metallised window.

## Why it works badly inside a train

A train carriage is a metal box, and metal blocks GPS signals. Your phone needs
line of sight to satellites, and the roof and walls provide none.

- **Sit by the window** and rest the phone against or near the glass.
- **Window films matter.** Many modern trains use metallised or heat-reflective
  glazing that attenuates GPS significantly. Some carriages simply will not work.
- **Tunnels** cut the fix completely. Readings resume after a short reacquisition
  delay on the other side.
- **Double-deck carriages** are worse on the lower deck.

If the Accuracy tile is showing hundreds of metres, you are not getting a real
fix and the speed figure is meaningless.

## Speed is not the same as average journey speed

A train that cruises at 160 km/h rarely averages anything close to it. Station
stops, signal checks, speed restrictions and approach curves pull the average
down hard — a service averaging 100 km/h door to door while peaking at 160 is
entirely normal.

Self Speed shows both: the live reading for the cruising figure, and a moving
average that excludes time spent stationary at platforms.

## Motion sickness

Reading a screen on a moving vehicle is a reliable way to feel unwell, because
your inner ear reports motion your eyes do not. Glance, don't stare — and the
max speed is recorded for you anyway.

## Getting a fix in each kind of vehicle

### Trains

The hardest case, because a carriage is effectively a Faraday cage. Press the
phone flat against the window if you can. Older rolling stock with plain glass
works noticeably better than modern air-conditioned stock with metallised
glazing, which can block the signal almost completely.

High-speed lines are often in cuttings, tunnels and noise-barrier corridors,
which is unfortunate given they are the services whose speed you most want to
measure. Expect intermittent readings.

### Buses and coaches

Generally better than trains. Buses have more glass relative to their size and
sit higher, and urban routes rarely reach speeds where you need precision. A
window seat gets a usable fix in most cases.

### Ferries

Excellent. Open deck, unobstructed sky, no interference — close to ideal GPS
conditions. Switch the units to knots for the reading the crew would use. See
[boat speedometer](/self-speed/boat-speedometer-knots/).

### Aircraft

Possible but awkward. Cabin windows are small, deeply recessed, and on many
aircraft treated with coatings that attenuate the signal. You need a window seat
and patience, and a fix acquired on the ground before takeoff is far more likely
to survive than one attempted at altitude.

Note also that most airlines' rules require flight mode, which on many devices
disables GPS along with the radios. Some devices let you re-enable location
separately in flight mode; check your own before assuming.

## Reading the numbers sensibly

A common confusion is comparing a live reading against a published service speed.
These measure different things:

| Figure | What it means |
|---|---|
| Live GPS speed | Your actual speed at this instant |
| Line speed | The maximum the track is signalled for |
| Service speed | What the train is scheduled to run at |
| Average journey speed | Total distance divided by total time, stops included |

A service advertised as "200 km/h" spends most of its journey well below that.
Line speed applies only to the sections engineered for it, and acceleration up to
it takes several minutes.

## Why the reading lags a real change

A GPS receiver applies its own filtering before reporting a velocity, and Self
Speed averages over a further 2.5 seconds. The combined effect is that a sharp
change — a train braking hard into a station — appears on screen a couple of
seconds after you feel it. That delay is the price of a stable number, and it is
a deliberate trade.
