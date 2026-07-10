Title: CVora — AI-powered career toolkit
Date: 2026-03-01
Tags: django, htmx, claude-api, fly.io
Summary: Full-stack AI career toolkit built and deployed in 3 days. ATS scoring against job descriptions, batch multi-JD comparison, interactive per-role resume coaching, and resume export as structured RenderCV YAML with PDF download.
Featured: true
Repo: https://github.com/picklecillo/bettercv
Demo: https://cvora.xyz

## What it does

CVora takes your resume and puts it to work against real job descriptions:

- **ATS scoring** — paste a job description, get a match score with a breakdown
  of what lands and what's missing.
- **Batch comparison** — score one resume against multiple job descriptions at
  once and see where you're strongest.
- **Per-role coaching** — an interactive session that walks through your resume
  in the context of a specific role and suggests concrete improvements.
- **Structured export** — resumes live as [RenderCV](https://rendercv.com)
  YAML, so output is versionable and renders to a clean PDF for download.

## How it's built

Django + HTMX on the backend-driven-UI end, the Claude API for the scoring and
coaching intelligence, deployed on Fly.io. From first commit to production in
three days.

The HTMX approach keeps the whole thing server-rendered: no SPA build step, no
client state to sync — every AI interaction is a partial swap.
