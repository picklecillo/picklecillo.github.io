# Portfolio

Personal portfolio and blog. Built with [Pelican](https://getpelican.com),
[Tailwind CSS v4](https://tailwindcss.com), and [daisyUI 5](https://daisyui.com).
Deployed to GitHub Pages via GitHub Actions.

## Local development

Requirements: Python 3.10+, Node 20+.

```console
$ python3 -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
$ npm install
```

Run two processes while developing:

```console
$ make css-watch    # rebuilds Tailwind CSS on template changes
$ make devserver    # builds + serves at http://localhost:8000, auto-reloads
```

One-off builds: `make css && make html`. Production build: `make publish`.

## Adding content

Content is plain Markdown with metadata headers. The folder decides the section.

**Blog post** — `content/blog/my-post.md`:

```markdown
Title: My post title
Date: 2026-07-10
Tags: python, testing
Summary: One-liner shown in listings and previews.

Body in Markdown...
```

**Project** — `content/projects/my-project.md`:

```markdown
Title: my-project — short tagline
Date: 2026-07-10
Tags: python, cli
Summary: What it is and why it exists.
Featured: true
Repo: https://github.com/picklecillo/my-project
Demo: https://example.com

Writeup in Markdown...
```

`Featured: true` puts a project on the landing page. `Repo`/`Demo` are optional
and render as icon links.

## Site data

Bio, experience timeline, social links, and contact email live in
`pelicanconf.py` (`BIO`, `EXPERIENCE`, `SOCIAL_LINKS`, `CONTACT_EMAIL`).

## Contact form

The form posts to [Formspree](https://formspree.io). Create a free form there
and put its ID in `FORMSPREE_ID` in `pelicanconf.py`.

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`: it builds the CSS and
site, then publishes `output/` to GitHub Pages.

One-time setup in the GitHub repo: **Settings → Pages → Source → GitHub Actions**.

The production URL is set in `publishconf.py` (`SITEURL`). If this repo is
renamed or moved to `picklecillo.github.io`, update it there.

## Theming

Two custom daisyUI themes (`light`/`dark`) are defined in `src/css/main.css` —
edit the OKLCH variables there to retheme. The navbar toggle persists the choice
in `localStorage` and defaults to the system preference.
