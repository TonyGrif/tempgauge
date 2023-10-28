import pytest
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
