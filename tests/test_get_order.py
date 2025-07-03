import requests

from data.urls import Urls
from data.responses import Responses


class TestGetOrder:
    def test_get_order_by_id_success(self):
        url = Urls.GET_ORDER_URL
        response = requests.put(url)

        assert response.status_code == 200
        assert 'order' in response.json()


    def test_get_order_by_id_no_id_error(self):
        url = Urls.ACCEPT_ORDER_URL
        response = requests.put(url)
        response_sample = Responses.GET_ORDER_NO_ID

        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    def test_get_order_by_id_wrong_id_error(self):
        url = Urls.ACCEPT_ORDER_URL
        response = requests.put(url)
        response_sample = Responses.GET_ORDER_WRONG_ID

        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']
