Title: this blog — the site you're looking at
Date: 2026-07-10
Tags: python, pelican, tailwind, daisyui, github.io
Summary: This portfolio itself. A markdown-driven static site built with Pelican, Tailwind CSS v4, and daisyUI 5, wearing a dark neubrutalist theme and deployed to GitHub Pages on every push.
Featured: true
Repo: https://github.com/picklecillo/picklecillo.github.io

## What it is

The site you're reading right now. Everything on it — the experience timeline,
the project cards, this very page — is generated from plain markdown files and
one Python config.

## The stack

- **[Pelican](https://getpelican.com)** — Python static site generator. Blog
  posts and project writeups are markdown files; the folder they live in
  (`content/blog/` or `content/projects/`) decides which section they land in.
- **[Tailwind CSS v4](https://tailwindcss.com) + [daisyUI 5](https://daisyui.com)**
  — all styling config lives in a single CSS file, no `tailwind.config.js`.
  The theme is one custom daisyUI theme: charcoal base, cream ink, hard green
  and loud yellow, zero border radius.
- **GitHub Actions → GitHub Pages** — every push to `main` builds the CSS and
  the site, then deploys. No servers, nothing to maintain.
- **[Formspree](https://formspree.io)** — the contact form on a static site,
  without publishing an email address anywhere.
- **[ghchart](https://ghchart.rshah.org)** — the contribution graph, flipped
  to dark mode with a CSS `invert` + `hue-rotate` trick.

## Design notes

The look is deliberate neubrutalism: 2px borders, hard offset shadows with no
blur, cards that physically press down on hover, Archivo Black shouting the
headlines while IBM Plex Mono handles the labels. One theme, executed hard —
no light/dark toggle to hedge with.

## Why a static site in 2026

Because a portfolio is mostly text that changes a few times a year. Markdown
in git, a build that takes half a second, free hosting, and nothing to patch
on a Tuesday night. Boring technology, chosen on purpose.
