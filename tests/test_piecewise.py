import pytest


from piecewise import piecewise_linear_interpolation


class TestPiecewiseLinearInterpolation:
    def test_equation(self):
        result = piecewise_linear_interpolation(30, 60, 80, 62)
        assert result == "98.0000 + -0.6000x"

        result = piecewise_linear_interpolation(30, 60, 77, 60)
        assert result == "94.0000 + -0.5667x"

        result = piecewise_linear_interpolation(0, 30, 61, 80)
        assert result == "61.0000 + 0.6333x"
