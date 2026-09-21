# Self Speed

A free GPS speedometer that runs entirely in your browser. No app install, no
account, and no location data ever leaves your device.

**Live:** https://selfspeed.app

## Features

- **Live speed** from the device GPS (`coords.speed`), falling back to haversine
  distance over elapsed time when the browser doesn't report speed directly
- **Units**: km/h, mph, m/s, knots — remembered between visits
- **Trip stats**: max, moving average, distance, elapsed time, GPS accuracy
- **Screen Wake Lock** so the display doesn't sleep mid-trip and kill tracking
- **Installable PWA** that works offline
- **Trip history** stored locally in your browser
- **GPX export** of your recorded track, for Strava, Garmin or any mapping tool

## Requirements

Needs GPS and a secure origin (`https://` or `localhost`). Works best on a phone
outdoors. Laptops usually derive position from Wi-Fi and report no speed at all —
the app detects this and says so rather than showing a misleading zero.

## Development

    python -m http.server 8000     # then open http://localhost:8000

Icons are generated, not checked in by hand:

    python tools/make_icons.py

## Roadmap

See [PLAN.md](PLAN.md).
