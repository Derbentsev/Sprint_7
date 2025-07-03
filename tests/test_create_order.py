import requests
import pytest

from data.urls import Urls
from data.data import Data


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

        url = Urls.CREATE_ORDER_URL

        response = requests.post(url, data=payload)
        assert response.status_code == 201
        assert 'track' in response.json()
