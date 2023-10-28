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
    temp_data = []

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
            # Stores as (time, [temps...])
            temp_data.append(f_temps)

    for core_num in range(len(temp_data[0][1])):
        print(f"Core {core_num} \n============")
        for count, _ in enumerate(temp_data):
            if count + 1 > len(temp_data) - 1:
                break

            start_time = temp_data[count][0]
            end_time = temp_data[count + 1][0]

            start_temp = temp_data[count][1][core_num]
            end_temp = temp_data[count + 1][1][core_num]

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
