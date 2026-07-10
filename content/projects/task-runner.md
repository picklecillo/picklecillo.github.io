Title: taskr — a minimal task runner
Date: 2026-05-12
Tags: python, cli, developer-tools
Summary: A zero-config task runner for Python projects. Define tasks as plain functions, run them from the terminal with automatic argument parsing.
Featured: true
Repo: https://github.com/picklecillo/taskr

## Why

Every project grows a pile of `scripts/` that nobody documents. Makefiles work, but
they're a second language with its own quoting rules. I wanted tasks that are just
Python functions.

## How it works

Define tasks in a `tasks.py` at the project root:

```python
from taskr import task

@task
def test(coverage: bool = False):
    """Run the test suite."""
    cmd = ["pytest"]
    if coverage:
        cmd += ["--cov", "src"]
    run(cmd)
```

Then run them:

```console
$ taskr test --coverage
```

Type hints become CLI flags. Docstrings become help text. No YAML, no config.

## What I learned

- `inspect.signature` gets you 90% of an argument parser for free
- Good error messages are most of the product in a CLI tool
- Shipping a tool with zero required config is a feature worth fighting for
