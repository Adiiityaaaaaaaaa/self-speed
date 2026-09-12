# Self Speed

A single-page speedometer that reads your live movement speed from the browser Geolocation API.

- Uses the device GPS speed reading (`coords.speed`) when available
- Falls back to haversine distance over elapsed time between fixes
- Units: km/h, mph, m/s, knots
- Tracks max speed, moving average, and total distance

Requires a secure origin (`https://` or `localhost`) and works best on a phone, outdoors.
