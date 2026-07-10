Title: home-dash — self-hosted home dashboard
Date: 2026-02-03
Tags: python, fastapi, raspberry-pi, htmx
Summary: A FastAPI + HTMX dashboard running on a Raspberry Pi: weather, calendar, transit times, and air quality on an e-ink display in the hallway.
Featured: true
Repo: https://github.com/picklecillo/home-dash
Demo: https://example.com/demo

## The setup

A Raspberry Pi Zero 2 W drives a 7.5" e-ink panel. The backend polls a handful of
APIs (weather, GTFS transit feed, Google Calendar) and renders a single server-side
page. HTMX handles partial refreshes on the interactive web version; the e-ink
display just screenshots the page every 15 minutes.

## Interesting problems

- **E-ink refresh budget**: full refreshes are slow and flashy, so the layout is
  designed around a stable grid where only text changes.
- **API rate limits on a home connection**: a tiny SQLite-backed cache with
  per-source TTLs keeps everything within free tiers.
- **Power loss resilience**: the whole thing is a systemd unit that rebuilds its
  state from cache on boot.

## Stack

FastAPI, HTMX, SQLite, Pillow for the e-ink render pass, systemd timers instead of
cron.
