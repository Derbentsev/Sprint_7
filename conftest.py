import pytest

from data.data import Data


@pytest.fixture
def courier_data():
    courier_data = {
        'login': Data.COURIER['login'],
        'password': Data.COURIER['password']
    }

    return courier_data
