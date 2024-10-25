"""This module contains the piecewise linear interpolation and
least squares approximation functionality.
"""

from typing import Tuple

import numpy as np


def piecewise_linear_interpolation(
    x_zero: int, x_one: int, y_zero: int, y_one: int
) -> Tuple[float, float]:
    """Calculate the piecewise linear interpolation for two points.

    Paramaters:
        x_zero (int): Starting time point.
        x_one (int): Ending time point.
        y_zero (int): Starting temperature.
        y_one (int): Ending temperature.

    Returns:
        values (tuple): The resulting y-intercept and slope.
    """
    slope = (y_one - y_zero) / (x_one - x_zero)

    y_intercept = y_zero - (slope * x_zero)

    return (y_intercept, slope)


def least_squares_transpose(
    x_matrix: np.ndarray, y_matrix: np.ndarray
) -> Tuple[float, float]:
    """Calculate the discrete least squares approximation for given points.

    Parameters:
        x_matrix (np.ndarray): The X matrix.
        y_matrix (np.ndarray): The Y matrix.

    Returns:
        values (tuple): The resulting y-intercept and slope.
    """
    x_transpose = np.transpose(x_matrix)
    xtx = np.dot(x_transpose, x_matrix)
    xty = np.dot(x_transpose, y_matrix)

    result_matrix = np.linalg.solve(xtx, xty)
    y_intercept = result_matrix[0][0]
    slope = result_matrix[1][0]

    return (y_intercept, slope)
