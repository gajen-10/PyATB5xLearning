import pytest

@pytest.fixture()
def Is_Married_before_run():
    return True

def test_update(Is_Married_before_run):
    assert Is_Married_before_run == True
    