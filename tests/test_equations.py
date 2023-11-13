import pytest

from equations import piecewise_linear_interpolation


class TestEquations:
    def test_piecewise_linear_interpolation(self):
        result = piecewise_linear_interpolation(30, 60, 80, 62)
        assert result == "98.0000 + -0.6000x"

        result = piecewise_linear_interpolation(30, 60, 77, 60)
        assert result == "94.0000 + -0.5667x"

        result = piecewise_linear_interpolation(0, 30, 61, 80)
        assert result == "61.0000 + 0.6333x"
