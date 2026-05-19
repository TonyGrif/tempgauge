"""This module contains the piecewise linear interpolation and
least squares approximation functionality.
"""

import math

import numpy as np


def piecewise_linear_interpolation(
    x_zero: float, x_one: float, y_zero: float, y_one: float
) -> tuple[float, float]:
    """Calculate the piecewise linear interpolation for two points.

    Args:
        x_zero: Starting time point.
        x_one: Ending time point.
        y_zero: Starting temperature.
        y_one: Ending temperature.

    Returns:
        values (tuple): The resulting y-intercept and slope.

    Raises:
        ValueError: If x_zero and x_one are equal.
    """
    if math.isclose(x_zero, x_one):
        raise ValueError("x_zero and x_one must be distinct")

    slope = (y_one - y_zero) / (x_one - x_zero)

    y_intercept = y_zero - (slope * x_zero)

    return (y_intercept, slope)


def least_squares_fit(
    x_matrix: np.ndarray, y_matrix: np.ndarray
) -> tuple[float, float]:
    """Calculate the discrete least squares approximation for given points.

    Args:
        x_matrix: The X matrix.
        y_matrix: The Y matrix.

    Returns:
        values (tuple): The resulting y-intercept and slope.

    Raises:
        numpy.linalg.LinAlgError: If the x-values are not distinct (singular matrix).
    """
    x_transpose = np.transpose(x_matrix)
    xtx = np.dot(x_transpose, x_matrix)
    xty = np.dot(x_transpose, y_matrix)

    result_matrix = np.linalg.solve(xtx, xty)
    y_intercept = result_matrix[0][0]
    slope = result_matrix[1][0]

    return (y_intercept, slope)
