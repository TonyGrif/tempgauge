from math import isclose

import numpy as np
import pytest

from temps.equations import least_squares_transpose, piecewise_linear_interpolation


@pytest.fixture
def x_matrix():
    return np.array([[1, 0], [1, 30], [1, 60], [1, 90], [1, 120]])


@pytest.fixture
def y_matrix():
    return np.array([[61], [80], [62], [83], [68]])


class TestEquations:
    def test_piecewise_linear_interpolation(self):
        result = piecewise_linear_interpolation(30, 60, 80, 62)
        assert isclose(result[0], 98.0000, rel_tol=1e-4)
        assert isclose(result[1], -0.6000, rel_tol=1e-4)

        result = piecewise_linear_interpolation(30, 60, 77, 60)
        assert isclose(result[0], 94.0000, rel_tol=1e-4)
        assert isclose(result[1], -0.5667, rel_tol=1e-4)

        result = piecewise_linear_interpolation(0, 30, 61, 80)
        assert isclose(result[0], 61.0000, rel_tol=1e-4)
        assert isclose(result[1], 0.6333, rel_tol=1e-4)

    def test_least_squares_transpose(self, x_matrix, y_matrix):
        result = least_squares_transpose(x_matrix, y_matrix)
        assert isclose(result[0], 67.4000, rel_tol=1e-4)
        # Odd case, equal right up to the 4th decimal place
        assert isclose(result[1], 0.0567, rel_tol=1e-3)

        x_matrix = np.array([[1, 0], [1, 1], [1, 2]])
        y_matrix = np.array([[0], [1], [4]])

        result = least_squares_transpose(x_matrix, y_matrix)
        assert isclose(result[0], -0.3333, rel_tol=1e-4)
        assert isclose(result[1], 2.0000, rel_tol=1e-4)

        x_matrix = np.array([[1, -2], [1, -1], [1, 0]])
        y_matrix = np.array([[4], [1], [0]])

        result = least_squares_transpose(x_matrix, y_matrix)
        assert isclose(result[0], -0.3333, rel_tol=1e-4)
        assert isclose(result[1], -2.0000, rel_tol=1e-4)
