---
title: How GPS Speedometers Work — Doppler Shift vs Position Differencing
description: How a GPS speedometer actually measures speed, why Doppler shift beats dividing distance by time, and what your phone is really doing when it reports a speed.
slug: how-gps-speedometers-work
priority: 0.8
---

# How GPS speedometers work

There are two completely different ways to get speed from GPS, and almost
everyone assumes the wrong one. The good method is far more accurate than most
people realise.

## The obvious method: position differencing

Take your position now, take it again a second later, measure the distance
between them, divide by the time. This is what you would write if you were asked
to build a speedometer in an afternoon.

It works, and it is what Self Speed falls back to when nothing better is
available. But it inherits every bit of the position error. If each fix is
accurate to ±5 m and they arrive a second apart, a stationary phone can appear to
move up to 10 m in a second — a phantom 36 km/h.

That error does not shrink with speed, so it matters most exactly when you are
moving slowly and want precision.

## The good method: Doppler shift

GPS satellites transmit at a known carrier frequency. As you move relative to a
satellite, the frequency you receive is shifted — the same effect that makes an
ambulance siren drop in pitch as it passes.

Your receiver measures that shift for every satellite it can see, typically eight
to twelve. Each gives one equation relating your velocity to the geometry of that
satellite. Solve the system and you get your velocity vector directly.

The crucial point: **this never uses your position at all.** It is an independent
measurement, derived from frequency rather than from location, so it does not
inherit position error.

| Method | Position differencing | Doppler |
|---|---|---|
| Measures | Distance ÷ time | Carrier frequency shift |
| Typical error | 1 – 5 m/s | 0.05 – 0.1 m/s |
| Needs previous fix | Yes | No |
| Accurate when stationary | No | Yes |
| Degrades in urban canyons | Yes | Yes, less so |

Doppler velocity is roughly **fifty times more accurate** than differencing
positions. A good receiver knows your speed to within a few centimetres per
second.

## Which one is your phone using?

The Web Geolocation API exposes this as `coords.speed`. When the receiver has
computed a Doppler velocity, that field contains it in metres per second. When it
has not, the field is empty.

Self Speed uses `coords.speed` whenever it is present and falls back to
differencing positions when it is not. The status line under the gauge tells you
which is active — it reads *GPS speed* for Doppler, *derived from position* for
the fallback.

In practice: **phones report Doppler speed, laptops and desktops do not.** A
laptop has no GPS chip at all; it derives position from nearby wifi networks,
which produces no velocity, which is why a desktop browser shows the fallback and
a reading that hovers near zero.

## Why your reading still jumps around

Even with Doppler, the displayed number moves. Three reasons:

1. **Satellite geometry changes.** Satellites set below the horizon and new ones rise. Each change slightly alters the solution.
2. **Multipath.** Signals bouncing off buildings arrive late, corrupting both position and velocity. This is why urban canyons are difficult.
3. **The receiver is filtering.** Most chipsets apply their own smoothing, and its behaviour changes with signal quality.

Self Speed averages readings over a 2.5 second window, which removes most visible
jitter while still responding within a couple of seconds to real changes.

## A brief history

Mechanical speedometers, patented by Otto Schulze in 1902, used a flexible cable
spinning a magnet inside an aluminium cup. Eddy currents dragged the cup around
against a hairspring, and the needle settled where the two forces balanced. Every
car used this for eighty years.

Electronic speedometers replaced the cable with a rotation sensor and a
microcontroller, but the principle was unchanged: count wheel rotations, multiply
by an assumed circumference.

GPS broke that chain entirely. For the first time, speed could be measured
without touching the vehicle — no calibration, no assumption about tyre size, no
mechanical wear. What you get is your genuine movement across the ground.
