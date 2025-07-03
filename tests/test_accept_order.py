import requests

from data.urls import Urls
from data.responses import Responses


class TestAcceptOrder:
    def test_accept_order_success(self):
        url = Urls.ACCEPT_ORDER_URL
        response = requests.put(url)

        assert response.status_code == 200
        assert response.json() == Responses.ACCEPT_ORDER_SUCCESS


    def test_accept_order_no_courier_id_error(self):
        url = Urls.ACCEPT_ORDER_URL
        response = requests.put(url)
        response_sample = Responses.ACCEPT_ORDER_NO_ID

        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    def test_accept_courier_wrong_courier_id_error(self):
        url = Urls.ACCEPT_ORDER_URL
        response = requests.put(url)
        response_sample = Responses.ACCEPT_ORDER_WRONG_ID

        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    def test_accept_order_no_order_id_error(self):
        url = Urls.ACCEPT_ORDER_URL
        response = requests.put(url)
        response_sample = Responses.ACCEPT_ORDER_NO_ID

        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    def test_accept_courier_wrong_order_id_error(self):
        url = Urls.ACCEPT_ORDER_URL
        response = requests.put(url)
        response_sample = Responses.ACCEPT_ORDER_WRONG_ID

        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']
