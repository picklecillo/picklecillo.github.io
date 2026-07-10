Title: logsample — smart log sampling proxy
Date: 2025-09-18
Tags: go, observability, infrastructure
Summary: A sidecar that samples application logs adaptively — keeps every error, dials noisy info logs down to a rate budget, and saves ~70% on log ingestion costs.
Repo: https://github.com/picklecillo/logsample

## The problem

Log ingestion pricing punishes chatty services. Most of the volume is repetitive
info-level noise, but naive sampling risks dropping the one error line you need
at 3am.

## The approach

`logsample` sits between the app and the log shipper:

1. **Errors and warnings always pass through.** Non-negotiable.
2. Info/debug lines are fingerprinted by template (message with numbers and IDs
   stripped) and each fingerprint gets a token bucket.
3. Dropped lines increment a counter that's flushed as a summary record, so you
   can still see *that* something was noisy, and how much.

## Results

On a staging cluster it cut ingested volume by ~70% with zero dropped
error-level events over a month of soak testing.
