#!/usr/bin/env python3
"""Count Unicode characters in a Goal text file or stdin."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8-sig")
    return sys.stdin.read()


def main() -> int:
    parser = argparse.ArgumentParser(description="Count Unicode characters in Goal text.")
    parser.add_argument("path", nargs="?", help="Optional path to a UTF-8 Goal text file. Reads stdin when omitted.")
    parser.add_argument("--limit", type=int, default=4000, help="Maximum allowed character count. Default: 4000.")
    args = parser.parse_args()

    text = read_text(args.path)
    count = len(text)
    print(f"characters: {count}")
    print(f"limit: {args.limit}")
    print(f"remaining: {args.limit - count}")

    if count > args.limit:
        print("status: over_limit")
        return 1

    print("status: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
