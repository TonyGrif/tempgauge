import pytest
import os.path
from core import Core


@pytest.fixture
def core():
    return Core(1)

@pytest.fixture
def full_core():
    core = Core(0)
    core.add_reading((0, 61))
    core.add_reading((30, 80))
    core.add_reading((60, 62))
    core.add_reading((90, 83))
    core.add_reading((120, 68))
    return core


class TestCore:
    def test_core_num(self, core):
        assert core.core_num == 1
        assert not core.readings

        core.core_num = 4
        assert core.core_num == 4
        assert not core.readings

        with pytest.raises(AttributeError):
            core.core_num = -3
            assert not core.readings

    def test_add_reading(self, core):
        assert core.core_num == 1
        assert not core.readings

        core.add_reading((30, 87))
        assert (30, 87) in core.readings

        core.add_reading((60, 73))
        assert (60, 73) in core.readings
        assert core.core_num == 1

    def test_str(self, full_core):
        string = str(full_core)
        assert "0" in string
        assert "30" in string
        assert "61.0000" in string
        assert "0.6333" in string
        assert "interpolation" in string

        assert "67.4000" in string
        assert "0.0567" in string
        assert "least-squares" in string

    def test_write_to_file(self, core):
        assert core.core_num == 1
        assert not core.readings

        core.add_reading((0, 61))
        core.add_reading((30, 80))
        core.add_reading((60, 62))
        core.add_reading((90, 83))
        core.add_reading((120, 68))

        core.write_to_file()
        assert os.path.isfile("reports/core-1.txt")

        with open("reports/core-1.txt", "r") as file:
            lines = file.readlines()
            assert "0" and "30" in lines[0]
            assert "61.0000" in lines[0]
            assert "0.6333" in lines[0]
            assert "interpolation" in lines[0]

            assert "0      <= x <=    120; y= 67.4000 + 0.0567x   ; least-squares" in lines[-1]
