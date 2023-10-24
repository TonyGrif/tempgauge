#!/usr/bin/env python3

"""This is the main module for the cpu-temperature project.
"""

import argparse
from pathlib import Path


from parse_temps import parse_raw_temps
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

    # TODO: restructure
    temp_data = []

    with open(args.txt_file, "r", encoding="utf-8") as temps:
        for f_temps in parse_raw_temps(temps):
            # Catch new lines at the end
            if not f_temps[1]:
                break
            temp_data.append(f_temps)

    for core_num in range(4):
        print(f"Core {core_num} \n============")
        for count, time in enumerate(temp_data):
            if count + 1 > len(temp_data) - 1:
                break

            start_time = temp_data[count][0]
            end_time = temp_data[count+1][0]

            start_temp = temp_data[count][1][core_num]
            end_temp = temp_data[count+1][1][core_num]

            print(
                f"{start_time} <= x <= {end_time}; "
                + f"y= {piecewise_linear_interpolation(start_time, end_time, start_temp, end_temp)}; "
                + "interpolation"
            )

        print("\n")

    return


if __name__ == "__main__":
    main()
