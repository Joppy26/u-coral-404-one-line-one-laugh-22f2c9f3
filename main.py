#!/usr/bin/env python3
"""One Line, One Laugh - make.fun bounty u-coral-404-one-line-one-laugh-22f2c9f3.

A deterministic program (Python 3.13, standard library only) that writes one
funny line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

No randomness, no wall clock, no network: two runs write identical bytes.
"""
import os

LINE = "I installed a doorbell camera for security; now I just watch my own packages get stolen in 4K."


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(outdir, "entry.txt")
    os.makedirs(outdir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path} ({len(LINE.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
