import pytest
import numpy as np

from equations import piecewise_linear_interpolation
from equations import least_squares_transpose

@pytest.fixture
def x_matrix():
    return np.array([[1, 0], [1, 30], [1, 60], [1, 90], [1, 120]])

@pytest.fixture
def y_matrix():
    return np.array([[61], [80], [62], [83], [68]])


class TestEquations:
    def test_piecewise_linear_interpolation(self):
        result = piecewise_linear_interpolation(30, 60, 80, 62)
        assert result == "98.0000 + -0.6000x"

        result = piecewise_linear_interpolation(30, 60, 77, 60)
        assert result == "94.0000 + -0.5667x"

        result = piecewise_linear_interpolation(0, 30, 61, 80)
        assert result == "61.0000 + 0.6333x"

    def test_least_squares_transpose(self, x_matrix, y_matrix):
        result = least_squares_transpose(x_matrix, y_matrix)
        assert result == "67.4000 + 0.0567x"

        x_matrix = np.array([[1, 0], [1, 1], [1, 2]])
        y_matrix = np.array([[0], [1], [4]])

        result = least_squares_transpose(x_matrix, y_matrix)
        assert result == "-0.3333 + 2.0000x"

        x_matrix = np.array([[1, -2], [1, -1], [1, 0]])
        y_matrix = np.array([[4], [1], [0]])

        result = least_squares_transpose(x_matrix, y_matrix)
        assert result == "-0.3333 + -2.0000x"
