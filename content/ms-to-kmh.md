---
title: m/s to km/h Converter — Metres per Second to Kilometres per Hour
description: Convert metres per second to km/h and mph. Multiply by 3.6. Full table, the derivation, and why scientists use m/s while road signs do not.
slug: ms-to-kmh
priority: 0.7
---

# m/s to km/h

**Multiply by 3.6.** To go back, divide by 3.6.

| m/s | km/h | mph |
|---|---|---|
| 0.5 | 1.8 | 1.1 |
| 1 | 3.6 | 2.2 |
| 1.5 | 5.4 | 3.4 |
| 2 | 7.2 | 4.5 |
| 3 | 10.8 | 6.7 |
| 4 | 14.4 | 8.9 |
| 5 | 18.0 | 11.2 |
| 6 | 21.6 | 13.4 |
| 8 | 28.8 | 17.9 |
| 10 | 36.0 | 22.4 |
| 15 | 54.0 | 33.6 |
| 20 | 72.0 | 44.7 |
| 30 | 108.0 | 67.1 |
| 50 | 180.0 | 111.8 |
| 100 | 360.0 | 223.7 |

## Where 3.6 comes from

There are 1,000 metres in a kilometre and 3,600 seconds in an hour. So:

> 1 m/s = 3,600 m/hour = 3.6 km/h

That is the whole derivation. The factor is exact, not rounded, which is why m/s
and km/h convert so cleanly compared with anything involving miles.

## Why science uses m/s

The metre per second is the **SI derived unit** for speed, and it is what every
physics equation expects. Acceleration is m/s², force calculations assume m/s,
and kinetic energy is ½mv² with v in m/s. Feed km/h into any of those and the
answer is wrong by a factor of 12.96.

Road signs use km/h purely because the numbers are more convenient for humans:
"50" reads better than "13.9".

## Reference points

| Reference | m/s | km/h |
|---|---|---|
| Comfortable walking | 1.4 | 5.0 |
| Brisk walking | 1.8 | 6.5 |
| Recreational running | 2.8 | 10.0 |
| Usain Bolt, peak | 12.4 | 44.7 |
| Urban speed limit | 13.9 | 50 |
| Motorway limit | 33.3 | 120 |
| Commercial airliner | 250 | 900 |
| Speed of sound, sea level | 343 | 1,235 |

## GPS reports speed in m/s

Worth knowing if you ever work with location data directly. The Web Geolocation
API's `coords.speed` field is **always in metres per second**, regardless of what
units the page displays.

Self Speed holds every internal calculation in m/s and converts only at the point
of display, which avoids compounding rounding errors across unit switches. You
can select m/s as a display unit directly if you prefer it.
