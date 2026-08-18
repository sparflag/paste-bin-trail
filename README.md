# Paste Bin Trail (`paste-bin-trail`)

**Category:** osint · **Difficulty:** easy · **Points:** 150

A public paste (or its cache/mirror) still holds the XOR key.

## Run it

```bash
docker build -t sparflag/paste-bin-trail .
# `deca-ai start paste-bin-trail` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is XOR-encrypted then base64-encoded. Discover the challenge key, then invert XOR+base64.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit paste-bin-trail 'sparflag{...}'
```

## Hints

- Search paste sites and Google Cache for the username/token given.
- The paste body is the key.
