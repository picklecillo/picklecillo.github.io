Title: The testing pyramid is a budget, not a law
Date: 2026-04-08
Tags: testing, python
Summary: Unit-heavy test suites optimize for the wrong failure mode in glue-code services. Here's how I decide where the tests go.

The classic pyramid says: lots of unit tests, some integration tests, few
end-to-end tests. Good advice for a compiler. Misleading for the average web
service, which is mostly *glue* — parse a request, call a database, call an API,
shape a response.

## Where glue code actually breaks

Glue breaks at the seams: the query that doesn't match the schema, the API
contract that changed, the serializer that drops a field. Unit tests with mocked
seams can't see any of that — they verify that the code agrees with your
assumptions, not with reality.

## My budget heuristic

For each module, ask: **what's the most expensive bug this could ship?**

- Pure logic (pricing rules, parsers, state machines) → unit tests, lots of them,
  property-based where inputs are adversarial.
- Database access → integration tests against a real PostgreSQL in Docker. Never
  mock the database you own.
- Third-party APIs → contract tests against recorded fixtures, plus one smoke
  test against the sandbox in CI.
- The whole request path → a handful of end-to-end tests for the money paths:
  signup, checkout, the webhook that bills people.

## The result

The suite ends up shaped less like a pyramid and more like an hourglass:
plenty of unit tests, a fat waist of integration tests, a few e2e. It's slower
than a mocked suite and catches roughly all of the bugs that used to page me.
