import requests
import pytest

from urls.urls import Urls
from data.data import Data


class TestOrderCreate:
    
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK', 'GREY'],
            ['BLACK'],
            ['GREY'],
            []
        ]
    )
    def create_order_success(color):
        payload = Data.ORDER
        payload['color'] = color

        url = Urls.CREATE_ORDER_URL

        response = requests.post(url, data=payload)
        assert response.status_code == 201
        assert response.json() == 'track'
