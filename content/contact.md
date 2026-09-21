---
title: Contact — Self Speed
description: How to get in touch about Self Speed, report a bug, or ask about the privacy policy.
slug: contact
priority: 0.4
---

# Contact

> **Site owner: replace this block with a working email address before
> publishing.** A reachable contact method is required by Google AdSense and is
> expected by most readers. This page will not pass review as it stands.

## Reporting a bug

The most useful bug report for a GPS tool includes:

- **Your device and browser**, for example iPhone 14 / Safari 17, or Pixel 8 /
  Chrome.
- **What the status line said** — *GPS speed* or *derived from position*.
- **What the accuracy figure showed** in metres.
- **Where you were** in general terms: open road, city centre, inside a train,
  under tree cover. Location context explains most speed problems.
- **What you expected versus what you saw.**

Speed readings that look wrong are very often a signal problem rather than a
software problem, and the accuracy figure usually reveals which.

## Issues on GitHub

Bugs and feature requests can also be raised directly at
[github.com/Adiiityaaaaaaaaa/self-speed](https://github.com/Adiiityaaaaaaaaa/self-speed/issues).

## Privacy questions

See the [privacy policy](/self-speed/privacy/). In short: your location is
processed on your device and never transmitted, and the site holds no personal
data about you at all.

## Before you report: common questions

Most reports we would receive turn out to be one of the following. Checking
these first will usually get you an answer faster than writing in.

### My speed shows zero even though I am moving

Look at the Accuracy tile. If it reads more than about 100 m, your device is not
getting a satellite fix — it is estimating position from nearby wifi networks or
your IP address, which produces no usable speed. This is the normal state of
affairs on a laptop or desktop, which have no GPS receiver at all.

Use a phone, go outdoors, and wait 30 to 60 seconds for the accuracy figure to
fall below about 15 m.

### Tracking stopped when I switched apps

Browsers suspend geolocation for pages that are not visible. This is a deliberate
platform privacy protection, not a bug, and it cannot be worked around from a web
page. iOS is particularly aggressive about it.

Keep Self Speed in the foreground while tracking. The page requests a screen wake
lock automatically so the display will not sleep on its own.

### My speed reading jumps around

GPS position error is a few metres, and when speed is computed from position that
error becomes a large apparent speed swing over short intervals. Self Speed
averages over 2.5 seconds to suppress this.

If it is still jumpy, you are likely somewhere with poor sky visibility — a city
street between tall buildings, under dense trees, or inside a vehicle. See
[is GPS speed accurate](/self-speed/is-gps-speed-accurate/).

### The number is lower than my car dashboard

That is expected and both readings are correct. Car speedometers are legally
required never to under-read, so manufacturers build in a margin of typically 3
to 7 percent. The full explanation is on the
[car speedometer](/self-speed/car-speedometer/) page.

### My distance is wrong

Distance is accumulated from your GPS track, and only counts movement that
exceeds the accuracy noise floor. In poor signal conditions, short distances get
discarded as noise and the total reads low. In very poor conditions, GPS drift
while stationary can make it read high.

### Does it work offline?

Yes, once you have loaded it once. The page caches itself in your browser, and
your GPS receiver does not need a data connection to get a fix — only to download
the page in the first place. Load it before you go up a mountain or out to sea.

### Is my location being uploaded?

No. There is no server. Everything is computed in your browser and nothing is
transmitted. See the [privacy policy](/self-speed/privacy/).
