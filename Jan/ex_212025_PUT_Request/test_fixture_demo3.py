import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_bookingid():
    return 123

def test_update_re1(create_token,create_bookingid):
    print("Token -->", create_token)
    print("Booking_ID---->" , create_bookingid)