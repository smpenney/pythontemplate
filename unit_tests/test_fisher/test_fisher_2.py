import pytest

from pythontemplate.algorithms import Fisher # pylint: disable=wrong-import-position, disable=import-error

@pytest.mark.unit
def test_fisher():
    """Unit test for the BaseLearner class
    """
    print("test_fisher")

    fisher = Fisher()
    assert fisher.test() == "test"
