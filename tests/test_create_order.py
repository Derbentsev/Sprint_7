import requests
import pytest

from data.urls import Urls
from data.data import Data
from helpers.helpers import Helpers


class TestCreateOrder:
    
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK', 'GREY'],
            ['BLACK'],
            ['GREY'],
            []
        ]
    )
    def test_create_order_success(self, color):
        payload = Data.ORDER
        payload['color'] = color

        response = Helpers.create_order(payload)
        assert response.status_code == 201
        assert 'track' in response.json()
