import requests

from data.urls import Urls
from data.data import Data
from data.responses import Responses
from helpers.helpers import Helpers


class TestGetOrder:
    def test_get_order_by_id_success(self):
        url = Urls.GET_ORDER_URL
        payload = Data.ORDER

        response = Helpers.create_order(payload)
        track = response.json()['track']

        response = requests.get(url, params={'t': track})
        print(response.url)

        assert response.status_code == 200
        assert 'order' in response.json()


    def test_get_order_by_id_no_id_error(self):
        url = Urls.GET_ORDER_URL
        response = requests.get(url)
        response_sample = Responses.GET_ORDER_NO_ID

        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    def test_get_order_by_id_wrong_id_error(self):
        url = Urls.GET_ORDER_URL
        response = requests.get(url, params={'t': 54784378})
        response_sample = Responses.GET_ORDER_WRONG_ID

        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']
