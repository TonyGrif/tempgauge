"""This module contains the piecewise linear interpolation and
least squares approximation functionality.
"""

import numpy as np


def piecewise_linear_interpolation(
    x_zero: int, x_one: int, y_zero: int, y_one: int
) -> str:
    """Calculate the piecewise linear interpolation for two points.

    Paramaters:
        x_zero (int): Starting time point.
        x_one (int): Ending time point.
        y_zero (int): Starting temperature.
        y_one (int): Ending temperature.

    Returns:
        equation (string): The resulting equation.
    """
    slope = (y_one - y_zero) / (x_one - x_zero)

    y_intercept = y_zero - (slope * x_zero)
    y_intercept = format(y_intercept, ".4f")

    equation = f"{y_intercept} + {format(slope, '.4f')}x"

    return equation


def least_squares_transpose() -> None:
    """Calculate the discrete least squares approximation for given points."""
    return None
