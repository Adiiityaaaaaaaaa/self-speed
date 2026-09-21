---
title: About Self Speed — A Free Browser GPS Speedometer
description: What Self Speed is, why it exists, how it works, and what it deliberately does not do.
slug: about
priority: 0.5
---

# About Self Speed

Self Speed is a free GPS speedometer that runs in a web browser. No app store, no
account, no install, no upload. You open a page, press a button, and see how fast
you are moving.

## Why it exists

Every phone already contains a GPS receiver capable of measuring speed to within
a fraction of a km/h. Getting that number should not require downloading an
application, creating an account, accepting a location-sharing agreement, and
watching a video advert.

It should require opening a web page. So that is what this is.

## How it works

The page uses the browser's standard Geolocation API. Where your device reports a
Doppler-derived velocity, Self Speed uses it directly — that is the accurate
method, and it is what phone GPS chips produce. Where it does not, the page falls
back to computing speed from the distance between successive positions.

The status line under the gauge always tells you which method is in use, and the
accuracy figure tells you how much to trust it. There is a longer explanation in
[how GPS speedometers work](/how-gps-speedometers-work/).

## What it does

- Live speed in km/h, mph, m/s or knots
- Maximum speed, moving average, distance and elapsed time
- A wake lock, so your screen does not sleep and kill tracking mid-trip
- Offline operation once loaded, for tunnels, mountains and open water
- Trip history, stored only in your own browser
- GPX export for Strava, Garmin, Komoot and anything else that reads the format

## What it deliberately does not do

- **No account.** There is nothing to sign up for.
- **No upload.** Your location never leaves your device. There is no server.
- **No tracking.** No analytics, no cookies, no third-party scripts.
- **No background tracking.** Browsers stop geolocation when a page is hidden.
  This is a platform limitation, and honestly a reasonable one.

## What it is not

It is not navigation equipment. It has no charts, no routing, no collision
avoidance and no redundancy, and it depends on a phone battery. For sailing,
aviation, or any situation where being wrong has consequences, carry proper
equipment.

It is also not a certified measuring instrument. Do not use it to contest a
speeding ticket.

## Open source

The site is a static page with no build step beyond a small Python script that
renders these articles. The source is on
[GitHub](https://github.com/Adiiityaaaaaaaaa/self-speed).
