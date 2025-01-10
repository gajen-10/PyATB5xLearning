import pytest

@pytest.fixture()
def before_run():
    return True

def test_update(before_run):
    assert before_run == True
