import pytest

from equations import piecewise_linear_interpolation
from equations import least_squares_transpose

@pytest.fixture
def points():
    points = [(30, 80), (60, 62)]
    return points

class TestEquations:
    def test_piecewise_linear_interpolation(self, points):
        result = piecewise_linear_interpolation(points[0][0], points[1][0], points[0][1], points[1][1])
        assert result == "98.0000 + -0.6000x"

        result = piecewise_linear_interpolation(30, 60, 77, 60)
        assert result == "94.0000 + -0.5667x"

        result = piecewise_linear_interpolation(0, 30, 61, 80)
        assert result == "61.0000 + 0.6333x"

    def test_least_squares_transpose(self, points):
        assert least_squares_transpose() is None
