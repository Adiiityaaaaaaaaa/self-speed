---
title: Privacy Policy — Self Speed
description: How Self Speed handles your location data. Short version: it never leaves your device, and there is no account, no server and no tracking.
slug: privacy
priority: 0.4
---

# Privacy policy

*Last updated: 22 September 2026*

## The short version

Self Speed asks for your location because a speedometer cannot work without it.
That location is used inside your browser, on your device, to calculate a number
on screen. **It is never transmitted anywhere.** There is no server to send it
to.

## Your location data

When you press Start, the page calls your browser's standard Geolocation API.
Your browser asks your permission, and if you grant it, supplies a stream of
position readings.

Those readings are used entirely within the page to compute your speed,
distance, elapsed time and track. They exist in your device's memory while the
page is open. When you close the tab, they are gone.

We do not upload them, log them, store them on any server, or share them with
anyone. There is no server-side component to this site — it is a static page.

## What is stored on your device

Two things are saved in your browser's local storage, which never leaves your
device and which we cannot read:

| What | Why | How to remove |
|---|---|---|
| Your preferred units | So the page opens in km/h or mph as you left it | Clear site data in your browser |
| Trip summaries | The Recent trips list: date, distance, max and average speed | Press Clear in the trips section |

Trip summaries contain **no coordinates** — only aggregate figures. Your actual
route is held in memory during a session for GPX export and is discarded when
you close the page.

## Offline caching

The site registers a service worker, which stores a copy of the page files in
your browser so it still works without a signal. This caches only the site's own
code and images. It stores nothing about you.

## Cookies and analytics

**This site currently sets no cookies and runs no analytics.** There is no
Google Analytics, no tracking pixel, no fingerprinting, and no third-party
scripts of any kind.

If advertising is introduced in future, this policy will be updated before it
goes live to describe exactly what is set and by whom, and a consent mechanism
will be provided where the law requires one.

## Hosting

The site is served as static files by its hosting provider. Like any web host,
that provider may log standard request data — IP address, timestamp, user agent —
as part of normal server operation. We do not have access to per-user logs of
this kind and do not use them.

## Your rights

Because we hold no personal data about you, there is nothing for us to disclose,
correct or delete on request. Everything the site knows about you is on your own
device, under your control, and removable by clearing your browser's site data.

## Children

This site is a general-purpose utility and is not directed at children. It
collects no data from anyone, of any age.

## Changes

Material changes to this policy will be reflected in the date at the top of this
page.

## Contact

Questions about this policy: see the [contact page](/contact/).
