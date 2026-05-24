"""This module is a collection of input helpers for the CPU Temperatures project."""

from collections.abc import Iterator
from typing import TextIO


def parse_raw_temps(
    original_temps: TextIO, step_size: int = 30
) -> Iterator[tuple[float, list[float]]]:
    """
    Take an input file and time-step size and parse all core temps.

    Args:
        original_temps: an input file

        step_size: time-step in seconds

    Yields:
        A tuple containing the next time step and a List containing _n_ core
        temps as floating point values (where _n_ is the number of CPU cores)

    Raises:
        ValueError: If any value in a line cannot be parsed as a float.
    """
    for step, line in enumerate(original_temps):
        yield (step * step_size), [float(v) for v in line.split()]
