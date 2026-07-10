Title: ClickDocs — export ClickUp docs as markdown
Date: 2026-05-01
Tags: python, django, tailwind, fly.io
Summary: A freemium web tool that exports ClickUp workspace docs as portable markdown files. Python library + CLI at the core, Django web UI on top, deployed on Fly.io.
Featured: true
Demo: https://clickdocs.xyz

## The problem

Teams write years of documentation into ClickUp, and then it lives there —
locked behind the app, unsearchable from the terminal, invisible to git, and
awkward to migrate. ClickDocs pulls it out: point it at a workspace and get
clean markdown files back.

## How it's structured

Two components in a UV workspace:

- **`clickup-exporter`** — a standalone Python library and CLI that walks the
  ClickUp API (docs, nested pages) and writes them out as markdown. Small
  dependency footprint: `requests` for the API, `mdutils` for generation.
- **`export-site`** — a Django + Tailwind web UI wrapping the library at
  [clickdocs.xyz](https://clickdocs.xyz): register, connect your workspace,
  export. Freemium — the first 10 pages are free.

Deployed on Fly.io with Docker.

## Interesting bits

- **Nested page trees** — ClickUp docs are hierarchical; mapping that onto a
  sane directory structure with correct relative links is most of the actual
  work.
- **API testing without the API** — the test suite uses `pytest-vcr` to record
  real ClickUp API responses once and replay them forever, so tests are fast
  and deterministic.
- **Library-first design** — the web product is a thin wrapper; anyone who'd
  rather stay in the terminal can use the CLI directly against their own API
  token.
