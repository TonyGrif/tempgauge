"""This module contains the CPU core class."""

from pathlib import Path

import numpy as np
import numpy.typing as npt

from .equations import least_squares_fit as lsf
from .equations import piecewise_linear_interpolation as pli


class Core:
    """Data structure containing data on a CPU core.

    Attributes:
        core_num: The CPU core number.
        readings: Collection of tuples containing (time, temperature) data.
    """

    def __init__(self, c_num: int) -> None:
        """Constructor for the Core class

        Args:
            c_num: The CPU core number.
        """
        self.core_num = c_num
        self.readings: list[tuple[float, float]] = []

    @property
    def core_num(self) -> int:
        """The core number this Core object."""
        return self._core_num

    @core_num.setter
    def core_num(self, num: int) -> None:
        """Set the core number of this Core.

        Args:
            num: The core number.

        Raises:
            ValueError: If negative number is passed.
        """
        if num < 0:
            raise ValueError("Negative core number is not allowed")
        self._core_num = num

    def add_reading(self, point: tuple[float, float]) -> None:
        """Add a new reading to the reading list.

        Args:
            point: Tuple containing (time, temperature) readings.
        """
        self.readings.append(point)

    def _to_numpy_arrays(
        self,
    ) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
        """Convert the reading points to x and y matrices.

        Returns:
            x_matrix (tuple[0]): The X matrix.
            y_matrix (tuple[1]): The Y matrix.
        """
        x_points = [[1, t] for t, _ in self.readings]
        y_points = [[temp] for _, temp in self.readings]

        return np.array(x_points), np.array(y_points)

    def __str__(self) -> str:
        """Return the string representation of this object.

        Returns:
            string (str): String representation
        """
        if len(self.readings) < 2:
            return ""

        lines = []

        for (start_time, start_temp), (end_time, end_temp) in zip(
            self.readings, self.readings[1:], strict=False
        ):
            y_int, slope = pli(start_time, end_time, start_temp, end_temp)
            sign = "+" if slope >= 0 else "-"
            lines.append(
                f"{start_time: <6} <= x <= {end_time: >6}; "
                f"y = {y_int:.4f} {sign} {abs(slope):.4f}; interpolation"
            )

        x_matrix, y_matrix = self._to_numpy_arrays()
        start_time = self.readings[0][0]
        end_time = self.readings[-1][0]
        y_int, slope = lsf(x_matrix, y_matrix)
        sign = "+" if slope >= 0 else "-"
        lines.append(
            f"{start_time: <6} <= x <= {end_time: >6}; "
            f"y = {y_int:.4f} {sign} {abs(slope):.4f}; least-squares"
        )

        return "\n".join(lines) + "\n"

    def write_to_file(self, directory: str | Path = "reports") -> None:
        """Write a core's calculations to file.

        Args:
            directory: The output directory.
        """
        Path(directory).mkdir(parents=True, exist_ok=True)

        with open(
            Path(directory) / f"core-{self.core_num}.txt", "w", encoding="UTF-8"
        ) as file:
            file.write(str(self))
