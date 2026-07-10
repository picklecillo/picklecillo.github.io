Title: Súbete Perra — local event discovery for Chile
Date: 2026-06-01
Tags: django, postgresql, tailwind, fly.io
Summary: A free event discovery platform for Chile — find what's happening near you, or publish your own event with zero friction. Django 6 on Python 3.13, PostgreSQL, deployed on Fly.io.
Featured: true
Demo: https://subeteperra.cl

## What it is

[subeteperra.cl](https://subeteperra.cl) helps people discover events happening
around them — music, arts, sports, tech, LGBTQIA+, food, and more — and lets
organizers publish events without fees or gatekeeping. Browse by category,
filter free events, reserve a spot, show up.

Fully bilingual (Spanish/English) via Django's i18n.

## The stack

- **Django 6.0 on Python 3.13**, dependencies managed with uv, everything
  running in Docker
- **PostgreSQL 17** behind the scenes, **Tailwind** on the front
- **Fly.io** for hosting, WhiteNoise for static files, Sentry for errors
- **geopy** powers the location-based discovery, **icalendar** exports events
  straight to your calendar
- **Claude API** in the mix for AI-assisted features
- **django-axes** rate-limits login attempts; **MessageBird** handles SMS

## Engineering notes

- **Tested end-to-end** — pytest + factory-boy for the unit/integration layer,
  Playwright driving a real browser for the flows that matter (browse →
  register → attend).
- **A companion Chrome extension** lives in the same repo for capturing events
  from around the web.
- **Boring, deployable architecture** — one Django app, one database, one
  `fly deploy`. No microservices for a product that fits in one head.
