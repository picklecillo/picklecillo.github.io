Title: Fichario — encrypted clinical records for therapists
Date: 2026-11-25
Tags: flutter, dart, libsodium, sqlite, local-first
Summary: Pickle Labs' first product. An offline-first app that keeps therapists' clinical records encrypted on their own devices, syncing through a folder they already use, with no server of ours in between. Built for Chile's new data protection law (Ley 21.719).
Featured: true
Demo: https://fichario.cl

## The problem

Chile's Ley 21.719 takes effect on **October 15, 2027**, and it classifies
health data as *sensitive*, the strongest protection the law defines. For therapists, looking after patient records
stops being good practice and becomes an obligation.

Most of them are solo practitioners: psychologists, physical therapists,
speech therapists, nutritionists. Records live in notebooks, spreadsheets, or
shared cloud folders. Nobody has an IT department, and nobody wants one.

## What Fichario is

- **Encrypted records.** Patients, sessions, and consent are encrypted at rest.
  Without the passphrase or the printed recovery key, nobody can read them,
  including us.
- **Offline-first, no Fichario server.** Each device keeps its own encrypted
  database. To use several devices, the practitioner picks a folder they
  already sync (Dropbox, iCloud Drive, OneDrive…) and Fichario writes a single
  encrypted file there. The sync provider only ever sees ciphertext.
- **Consent with a paper trail.** What each patient agreed to, when, how, and
  which version of the text.
- **No accounts, no telemetry.** "Data Not Collected" on every store.
- **Pricing.** 30-day free trial, then a one-time purchase. No subscription.

## How it's built

**Flutter**, one codebase for macOS, Windows, iPad, iPhone, and Android.

**Crypto** is libsodium:

- Argon2id turns the passphrase into a key-encryption key. Its cost is tuned
  at vault creation to take about a second on the device.
- That key, and a second one derived from a random 128-bit recovery key, each
  wrap a random data key. The data key is never derived from the passphrase,
  so changing the passphrase doesn't mean re-deriving everything.
- Records are sealed with XChaCha20-Poly1305. The vault file's header (KDF
  params, wrapped keys) is bound in as additional authenticated data, so it
  can't be tampered with, and it holds no patient data at all.

**Storage** is drift on SQLite3MultipleCiphers. The local database is
encrypted with a key derived from the same data key, and it fails closed if
the cipher build is missing.

**Sync** never puts a live SQLite file in the shared folder, because sync
tools corrupt them and iPad file providers don't support locking. Each device
instead merges a snapshot file record by record. The last edit wins per
patient or session, not per file, so editing patient A on the iPad and
patient B on the laptop never loses either. Conflict copies left by sync
tools get merged and cleaned up. Writes go to a temp file followed by an
atomic rename.

## The hard part

Crypto libraries are the easy part. The hard part is everything a server
would normally handle for you, made safe for someone who will never read a
security FAQ:

- **Losing the passphrase.** A recovery key gets printed at setup, and the
  app makes you re-type part of it before it'll continue.
- **Changing the passphrase.** This generates a new data key and re-encrypts
  the database by copying it to a new file. That's crash-safe at every step,
  and the other devices pick up the new credentials on their next sync.
- **Old devices coming back online.** Deletion markers are kept forever, so a
  laptop that was off for months can't bring deleted patients back.
- **Never leaking by accident.** App code is not allowed to log anything, and
  CI enforces it.

## Being honest about compliance

No software can make you compliant on its own. That also depends on how a
practice works. Fichario's job is to make the compliant path the easy
one, without pretending to be a checkbox.

## Status

Finishing the first version. The waitlist is open at
[fichario.cl](https://fichario.cl).
