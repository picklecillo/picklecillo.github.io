Title: Why I still bet on boring technology
Date: 2026-06-20
Tags: engineering, opinion
Summary: New tools are fun, but most of my best production decisions were choosing the boring option: PostgreSQL over the shiny thing, monolith over microservices, cron over a workflow engine.

Every few months a new tool promises to change how we build software. Some of them
do! But after a few years of carrying a pager, my heuristic has hardened: **choose
boring technology unless you can name the specific problem the exciting one
solves for you.**

## The innovation budget

Dan McKinley's framing still holds up: every team gets a limited number of
innovation tokens. Spend them on the thing that differentiates your product, not
on the queueing system.

## Where this has paid off

- **PostgreSQL for everything** — queue, cache, search, and JSON documents, until
  the numbers said otherwise. The numbers usually never said otherwise.
- **A monolith with good module boundaries** beat the microservices refactor we
  almost did in 2021. The boundaries were the valuable part; the network hops
  were not.
- **Cron and a table of jobs** instead of a workflow engine. When we finally
  outgrew it, the migration was easy *because* the system was simple.

## Where it hasn't

Boring isn't a religion. When we actually hit the wall — multi-region writes,
sub-second analytics on billions of rows — the exciting tool earned its place.
The point is that it had to earn it.
