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
`pelicanconf.py` (`BIO`, `EXPERIENCE`, `SOCIAL_LINKS`). No email address is
published anywhere on the site — contact goes through the Formspree form.

## Contact form

The form posts to [Formspree](https://formspree.io). Create a free form there
and put its ID in `FORMSPREE_ID` in `pelicanconf.py`.

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`: it builds the CSS and
site, then publishes `output/` to GitHub Pages.

Pages is configured with **GitHub Actions** as the source (Settings → Pages).

The production URL (`https://picklecillo.github.io`) is set in `publishconf.py`
(`SITEURL`).

## Theming

A single neubrutalist daisyUI theme (`brut`) is defined in `src/css/main.css` —
cream base, near-black ink, hard green primary and yellow secondary, zero border
radius. Edit the OKLCH variables there to retheme. The brutalist primitives
(`brut-border`, `brut-shadow`, `brut-press`, `section-label`, `hl`) live in the
same file.
