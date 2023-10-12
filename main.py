#!/usr/bin/env python3

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
            prog="cpu-temperature",
            description="Python program to analyze CPU temperature changes over time")

    parser.add_argument(
            'txt_file',
            type=Path,
            help="Path to text file")

    args = parser.parse_args()

    if not args.txt_file.is_file():
        print("Must supply a real text file")
        return

    return

if __name__ == "__main__":
    main()
