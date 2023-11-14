import pytest
import os.path
from core import Core


@pytest.fixture
def core():
    return Core(1)


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
            assert (
                "0      <= x <=     30; y= 61.0000 + 0.6333x   ; interpolation"
                in lines[0]
            )
            assert "0<=x<=120;y=67.4000 + 0.0567x;least-squares" in lines[-1]
