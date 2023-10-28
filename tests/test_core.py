import pytest
from core import Core


@pytest.fixture
def core():
    return Core(1)


class TestCore:
    def test_core_num(self, core):
        assert core.core_num == 1

        core.core_num = 4
        assert core.core_num == 4

        with pytest.raises(AttributeError):
            core.core_num = -3

    def test_readings(self, core):
        pass
