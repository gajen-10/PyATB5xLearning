import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_bookingID():
    return 1

@pytest.fixture()
def read_excel_file():
    return"xyz"

def test_put(create_token,create_bookingID):
    print(create_token)
    print(create_bookingID)

def test_put2(create_token,create_bookingID,read_excel_file):
    print(create_token)
    print(create_bookingID)
    print(read_excel_file)