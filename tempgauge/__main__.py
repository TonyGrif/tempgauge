#!/usr/bin/env python3

"""This is the main module for the cpu-temperature project."""

import argparse
from pathlib import Path

from tempgauge import Core, parse_raw_temps


def main() -> None:
    """Run the cpu-temperature program."""
    parser = argparse.ArgumentParser(
        prog="cpu-temperature",
        description="Analyzes CPU temperature changes over time",
    )

    parser.add_argument("txt_file", type=Path, help="Path to text file")

    args = parser.parse_args()

    if not args.txt_file.is_file() or args.txt_file.suffix.lower() != ".txt":
        parser.error("Must supply a real text file")

    cores = []

    with open(args.txt_file, encoding="utf-8") as temps:
        core_count = len(temps.readline().split())

        for core_num in range(core_count):
            cores.append(Core(core_num))

        temps.seek(0)

        for time_step, readings in parse_raw_temps(temps):
            if not readings:
                continue

            for core_idx, temp in enumerate(readings):
                cores[core_idx].add_reading((time_step, temp))

    for core in cores:
        core.write_to_file()


if __name__ == "__main__":
    main()
