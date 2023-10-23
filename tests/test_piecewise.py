import pytest


from piecewise import piecewise_linear_interpolation

class TestPiecewiseLinearInterpolation:
    def test_equation(self):
        result = piecewise_linear_interpolation(30, 60, 80, 62)
        assert result == "98.0 + -0.6x"
