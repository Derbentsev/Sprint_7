import requests

from data.urls import Urls
from data.data import Data
from helpers.helpers import Helpers


class TestOrderList:
    
    def test_get_orsers_list_success(self):
        courier_data = {
            'login': Data.COURIER['login'],
            'password': Data.COURIER['password']
        }

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == 200
        courier_id = response.json()['id']

        params = {
            'courierId': courier_id,
            'nearestStation': ["1"],
            'limit': 10,
            'page': 0
        }

        url = Urls.GET_ORDER_LIST_URL

        response = requests.get(url, params=params)
        assert response.status_code == 200
        assert 'orders' in response.json()
