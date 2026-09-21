---
title: Boat Speedometer in Knots — GPS Speed Over Ground for Sailing
description: A free GPS speedometer in knots for sailing, motorboating and kayaking. Shows speed over ground, distance in nautical miles, and works offline on the water.
slug: boat-speedometer-knots
priority: 0.9
---

# Boat speedometer — knots

Switch the units to **knots** and Self Speed becomes a GPS speed-over-ground
readout for sailing, motorboating, kayaking or paddleboarding. Distance is
reported in nautical miles to match.

## Speed over ground is not speed through water

This distinction matters more on the water than anywhere else, and it is the
single most useful thing GPS gives a sailor.

- **Speed through water (STW)** is what a paddlewheel or impeller log measures:
  how fast the hull moves relative to the water around it.
- **Speed over ground (SOG)** is what GPS measures: how fast you move relative
  to the seabed.

The difference between them *is the current*. Sail at 6 knots through the water
against a 2 knot foul tide and your GPS reads 4 knots over ground. Turn around
and it reads 8.

> If your log says 6 and your GPS says 4, you are not slow — you have two knots
> of tide against you. Navigating on STW alone in tidal waters will put you
> somewhere you did not intend.

## Why passage planning uses SOG

Your estimated time of arrival depends entirely on speed over ground, because
that is what closes the distance to your destination. A tidal gate you need to
make at a particular hour is a SOG calculation, not a STW one.

| Metric | Source | Use it for |
|---|---|---|
| Speed over ground | GPS | ETA, passage planning, tidal gates |
| Speed through water | Paddlewheel log | Sail trim, boat performance |
| Both together | — | Working out the set and drift of the current |

## Units and conversions

One knot is one nautical mile per hour — and one nautical mile is one minute of
latitude, which is why the unit survives. It is 1.852 km/h exactly.

| Knots | km/h | mph |
|---|---|---|
| 1 | 1.85 | 1.15 |
| 3 | 5.56 | 3.45 |
| 5 | 9.26 | 5.75 |
| 6 | 11.11 | 6.90 |
| 10 | 18.52 | 11.51 |
| 20 | 37.04 | 23.02 |
| 30 | 55.56 | 34.52 |

## GPS at sea is unusually good

Open water is the ideal GPS environment — total sky visibility, no buildings, no
tree cover, no multipath reflections off nearby surfaces. Accuracy at sea is
typically better than anywhere on land, often ±3 m or better.

The practical problems are different: **salt water and phones do not mix**, and
you will frequently be out of mobile data range. Self Speed works offline once
loaded, so open it before you leave the dock and it keeps running with no signal.

## A serious caveat

This is a convenience tool, not navigation equipment. It has no chart, no AIS,
no depth, no collision avoidance and no redundancy — and a phone battery dies.
Carry proper navigation equipment and paper charts for any passage where getting
it wrong has consequences.

## Working out the current

If you have both a log and GPS, the current falls straight out of the difference,
and knowing it changes your decisions.

Sailing a course with speed through water of 6.0 knots and speed over ground of
4.2 knots means 1.8 knots of foul tide. Over a six-hour passage that is nearly 11
nautical miles of lost ground — frequently the difference between arriving on the
tide and waiting outside a harbour for six hours.

Tidal streams in constricted waters run far harder than open-sea figures suggest.
The Pentland Firth reaches 12 knots on springs, faster than most cruising yachts
can sail. There, the tide decides whether the passage is possible at all.

## Hull speed

A displacement hull is limited by the wave it makes. As it approaches the speed
at which its own bow wave is as long as the hull, the boat is climbing a hole of
its own digging, and power requirements rise steeply.

> Hull speed in knots is roughly 1.34 times the square root of the waterline
> length in feet.

| Waterline | Hull speed |
|---|---|
| 20 ft | 6.0 knots |
| 25 ft | 6.7 knots |
| 30 ft | 7.3 knots |
| 40 ft | 8.5 knots |

This is why boat speed is so tightly linked to length, and why a 40-footer is
only modestly faster than a 30-footer despite being far larger. Planing hulls and
multihulls escape the limit by rising over their own bow wave instead of pushing
through it.

## Frequently asked

### Why does my GPS speed differ from my log?

The difference is the current. GPS measures speed over ground, the log measures
speed through water. Both are correct, and the gap between them is the useful
information.

### Is GPS accurate at sea?

Unusually so. Open water gives total sky visibility with no buildings, trees or
reflecting surfaces, so accuracy is typically better than anywhere on land.

### Will it work out of mobile range?

Yes. GPS satellites are not mobile networks, and your receiver needs no data
connection to get a fix. Load the page before leaving the dock and it works
offline for the whole passage.

### Can I use it for navigation?

No. It has no chart, no depth, no AIS, no collision avoidance and no redundancy,
and it depends on a phone battery in a wet environment. Carry proper navigation
equipment.
