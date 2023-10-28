#!/usr/bin/env python3

"""This is the main module for the cpu-temperature project.
"""

import argparse
from pathlib import Path

from parse_temps import parse_raw_temps
from src.core import Core
from src.piecewise import piecewise_linear_interpolation


def main():
    """Run the cpu-temperature program."""
    parser = argparse.ArgumentParser(
        prog="cpu-temperature",
        description="Analyzes CPU temperature changes over time",
    )

    parser.add_argument("txt_file", type=Path, help="Path to text file")

    args = parser.parse_args()

    if not args.txt_file.is_file() or args.txt_file.suffix != ".txt":
        print("Must supply a real text file")
        return

    cores = []

    with open(args.txt_file, "r", encoding="utf-8") as temps:
        # Get number of cores, create structure for each, then go back
        last_line = temps.tell()
        count = len((temps.readline()).split())

        for core_num in range(count):
            cores.append(Core(core_num))

        temps.seek(last_line)

        # Parse data
        for f_temps in parse_raw_temps(temps):
            # Catch new lines at the end
            if not f_temps[1]:
                break

            for count, temp in enumerate(f_temps[1]):
                cores[count].add_reading((f_temps[0], temp))

    for core in cores:
        print(f"Core {core.core_num} \n=======")

        for count, _ in enumerate(core.readings):
            if count + 1 > len(core.readings) - 1:
                break

            start_time = core.readings[count][0]
            end_time = core.readings[count + 1][0]
            start_temp = core.readings[count][1]
            end_temp = core.readings[count + 1][1]

            pli_eq = piecewise_linear_interpolation(
                start_time, end_time, start_temp, end_temp
            )

            print(
                f"{start_time: <6} <= x <= {end_time: >6}; "
                + f"y= {pli_eq: <20}; "
                + "interpolation"
            )

        print("\n")

    return


if __name__ == "__main__":
    main()
