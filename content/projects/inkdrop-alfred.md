Title: ink+ — create Inkdrop notes from Alfred
Date: 2024-09-26
Tags: php, alfred, open-source, contribution
Summary: Open-source contribution to the official Inkdrop Alfred workflow — a new ink+ command that creates notes straight from the Alfred bar, with configurable default notebook and tags.
Repo: https://github.com/inkdropapp/inkdrop-alfred-workflow/pull/4

## The itch

The official [Inkdrop](https://www.inkdrop.app) Alfred workflow could only
*search* notes. Capturing a thought still meant switching to the app, finding
the right notebook, making a note — enough friction to lose the thought.

## The contribution

[Merged PR #4](https://github.com/inkdropapp/inkdrop-alfred-workflow/pull/4)
adds an `ink+` command: type `ink+ title: contents` and the note lands in
Inkdrop without ever leaving the keyboard.

![Alfred bar showing ink+ command creating a new Inkdrop note]({static}/images/inkdrop-alfred-ink-plus.png)

What went in:

- **`ink+ <title>:<contents>`** — new command hitting Inkdrop's local server
  API to create the note.
- **`defaultNotebook` and `defaultTags`** workflow environment variables, so
  captured notes are filed and tagged automatically.
- **Refactor** — `search.php` became `inkdrop.php`, since the workflow was no
  longer just search.
- **Failure feedback** — a macOS notification when the local server errors
  out, instead of silently eating the note.

## Why it's on this list

Small diff, daily payoff — this is the kind of tooling contribution I enjoy:
find the friction in a tool you actually use, remove it upstream so everyone
gets the fix.
