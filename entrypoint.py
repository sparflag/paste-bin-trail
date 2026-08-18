#!/usr/bin/env python3
"""Paste Bin Trail — real mini-challenge (paste-bin-trail)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'expired-paste')


def main():
    mat = fetch_material()
    key = CHALLENGE_KEY or "paste-key"
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    paste = (
        "=== paste.txt (expired but CDN-cached) ===\n"
        "status: expired (404 on origin)\n"
        "cache_hit: true\n"
        "ttl_remaining: 3600\n"
        "--- body ---\n"
        f"deploy token = {key}\n"
        "rotate after use\n"
        "---\n"
    )
    with open("/challenge/paste.txt", "w") as fh:
        fh.write(paste)
    print("Paste Bin Trail — cached paste.txt body still contains deploy token.")


if __name__ == "__main__":
    main()
