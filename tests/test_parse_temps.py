import io

import pytest

from tempgauge.parse_temps import parse_raw_temps


class TestParseRawTemps:
    def test_basic_parsing(self):
        data = io.StringIO("61.0 63.0 50.0 58.0\n80.0 81.0 68.0 77.0\n")
        results = list(parse_raw_temps(data))
        assert len(results) == 2
        assert results[0] == (0, [61.0, 63.0, 50.0, 58.0])
        assert results[1] == (30, [80.0, 81.0, 68.0, 77.0])

    def test_custom_step_size(self):
        data = io.StringIO("61.0 63.0\n80.0 81.0\n62.0 63.0\n")
        results = list(parse_raw_temps(data, step_size=60))
        assert results[0][0] == 0
        assert results[1][0] == 60
        assert results[2][0] == 120

    def test_single_core(self):
        data = io.StringIO("72.0\n75.0\n")
        results = list(parse_raw_temps(data))
        assert results[0] == (0, [72.0])
        assert results[1] == (30, [75.0])

    def test_empty_line_produces_empty_list(self):
        data = io.StringIO("61.0 63.0\n\n80.0 81.0\n")
        results = list(parse_raw_temps(data))
        assert results[1][1] == []

    def test_decimal_values_preserved(self):
        data = io.StringIO("65.5 70.2\n")
        results = list(parse_raw_temps(data))
        assert results[0][1] == [65.5, 70.2]

    def test_non_numeric_raises(self):
        data = io.StringIO("not_a_number\n")
        with pytest.raises(ValueError):
            list(parse_raw_temps(data))
