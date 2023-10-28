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

        core.core_num = -3
        assert core.core_num == 3
