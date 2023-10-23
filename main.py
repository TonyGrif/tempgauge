#!/usr/bin/env python3

"""This is the main module for the cpu-temperature project.
"""

import argparse
from pathlib import Path


from parse_temps import parse_raw_temps


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
    time = []
    core1 = []
    core2 = []
    core3 = []
    core4 = []
    with open(args.txt_file, 'r') as temps:
        # Output as one strucutre for now
        for f_temps in parse_raw_temps(temps):
            time.append(f_temps[0])
            core1.append(f_temps[1][0])
            core2.append(f_temps[1][1])
            core3.append(f_temps[1][2])
            core4.append(f_temps[1][3])

    print(time)
    print(core1)
    print(core2)
    print(core3)
    print(core4)

    return


if __name__ == "__main__":
    main()
