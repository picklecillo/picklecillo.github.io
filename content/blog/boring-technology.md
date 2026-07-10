Title: Boring technology, on purpose
Date: 2026-07-10
Tags: engineering, opinion, django, htmx
Summary: Everything I ship is Django, server-rendered, HTMX where it needs to feel alive. Not because I can't do the other thing — because nothing I build needs it.

Everything I ship lately is Django, server-rendered, HTMX where it needs to
feel alive. No SPA, no build step, no client state to sync.

Not a limitation. A choice.

## The receipts

[CVora](/projects/cvora-ai-powered-career-toolkit/) went from first commit to
production in three days. Part of that is the stack having no moving parts I
don't fully understand: Django views, HTMX partial swaps, one database,
`fly deploy`. Every AI interaction on that site is a server round-trip that
swaps a chunk of HTML. Nobody notices. Nobody cares. It ships.

This site: markdown files and [Pelican](/projects/this-blog-the-site-youre-looking-at/).
Builds in half a second. Hosting is free. A portfolio is text that changes a
few times a year — a React framework here would be decoration.

## The rule

New tech has to name the specific problem it solves for me, today, in this
product. "We might need it later" doesn't count.

The part people miss: when *later* actually arrives, migrating away from the
simple thing is easy — precisely because it's simple. Migrating away from the
complicated thing you adopted early is the expensive move.

## Not a religion

Sometimes the exciting tool wins. It just has to earn the spot with a problem
I can point at, not a feeling that I'm falling behind.

The stack is not the product. Shipping is the product.
