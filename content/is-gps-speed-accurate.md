---
title: Is GPS Speed Accurate? What Affects It and When to Trust It
description: How accurate GPS speed really is, what degrades it, and when you should trust your phone over your car dashboard. With typical error figures for each condition.
slug: is-gps-speed-accurate
priority: 0.8
---

# Is GPS speed accurate?

Short answer: **yes, usually more accurate than your car's speedometer** — but
only when it has a clear view of the sky, and it fails in specific, predictable
ways.

## Typical accuracy

With a good fix and a modern phone using Doppler velocity, speed error is around
**0.05 to 0.1 m/s**, which is under 0.4 km/h. That is better than any mechanical
speedometer ever built.

| Condition | Speed accuracy | Position accuracy |
|---|---|---|
| Open sky, stationary, good fix | ±0.1 km/h | ±3 – 5 m |
| Open road, moving, clear sky | ±0.2 – 0.5 km/h | ±5 m |
| Light tree cover | ±1 – 2 km/h | ±10 – 20 m |
| Urban canyon, tall buildings | ±3 – 10 km/h | ±20 – 50 m |
| Inside a train or building | unusable | ±50 – 500 m |
| No GPS chip, wifi positioning | meaningless | ±100 – 5,000 m |

## What degrades it

**Blocked sky.** The single biggest factor. Fewer visible satellites means a
weaker geometric solution. Tunnels, deep valleys, dense forest, inside vehicles.

**Multipath.** Signals reflect off buildings and arrive slightly late, so the
receiver computes a position that is subtly wrong. Glass-and-steel city centres
are the classic case, and it is why your position sometimes shows you inside a
building across the street.

**Cold starts.** A receiver that has not been used recently does not know which
satellites to look for and must download orbital data first. Give it 30 to 60
seconds outdoors before trusting the numbers.

**Very low speeds.** Walking pace is genuinely hard. The signal you are trying to
measure sits close to the noise floor, which is why a stationary phone sometimes
shows 2 km/h.

## How to tell if your reading is good

Watch the **Accuracy** tile. It reports the receiver's own confidence in metres.

- **±3 to 10 m** — a real satellite fix. Trust the speed.
- **±20 to 50 m** — degraded. Speed is indicative, not precise.
- **Over ±100 m** — this is not GPS. Your position came from wifi or your IP address, and the speed figure means nothing.

Self Speed shows a warning banner automatically when accuracy is worse than
200 m, because at that point the number on screen is not measuring anything real.

## GPS versus your car's dashboard

Your car reads high by design — legally it must never under-read, so
manufacturers build in a 3 to 7 percent margin. See [car speedometer](/self-speed/car-speedometer/)
for the regulation and the numbers.

So when GPS says 96 and the dashboard says 100, both are working correctly. GPS
is the more accurate measurement of your true speed.

**But drive by the dashboard anyway.** GPS drops out in tunnels and cities, and a
speedometer that occasionally stops working is not something to steer by. Use GPS
to learn your car's offset, then trust the dial.

## When GPS is definitively better

- Checking your car's speedometer error
- Sailing, where speed over ground is what you actually need
- Any vehicle with modified wheels or tyres
- Cycling without a calibrated wheel sensor
- Anything where you need distance as well as speed

## When to distrust it

- Indoors, or inside any metal vehicle
- On a running track, where the tight bends defeat it
- At walking pace
- In a narrow city street lined with tall glass buildings
- Whenever the accuracy figure is above about 50 m
