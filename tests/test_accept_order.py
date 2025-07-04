import requests

from data.data import Data
from data.urls import Urls
from data.responses import Responses
from helpers.helpers import Helpers


class TestAcceptOrder:
    def test_accept_order_success(self):
        courier_data = {
            'login': Data.COURIER['login'],
            'password': Data.COURIER['password']
        }

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == 200
        courier_id = response.json()['id']

        response = Helpers.create_order(Data.ORDER)
        assert response.status_code == 201
        order_track = response.json()['track']

        url = Urls.get_order_by_track_url(order_track)
        response = requests.get(url)
        assert response.status_code == 200
        order_id = response.json()['order']['id']

        url = Urls.get_accept_order_url(courier_id, order_id)        
        response = requests.put(url)
        assert response.status_code == 200
        assert response.json() == Responses.ACCEPT_ORDER_SUCCESS


    def test_accept_order_no_courier_id_error(self):
        url = Urls.ACCEPT_ORDER_URL
        response = requests.put(url)
        response_sample = Responses.ACCEPT_ORDER_NO_ID_COURIER

        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    def test_accept_courier_wrong_courier_id_error(self):
        url = Urls.get_accept_order_url(213, 852)
        response = requests.put(url)
        response_sample = Responses.ACCEPT_ORDER_WRONG_ID_COURIER

        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    def test_accept_order_no_order_id_error(self):
        courier_data = {
            'login': Data.COURIER['login'],
            'password': Data.COURIER['password']
        }

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == 200
        courier_id = response.json()['id']
    
        url = Urls.get_accept_order_url(courier_id, order_id='')
        response = requests.put(url)
        response_sample = Responses.ACCEPT_ORDER_NO_ID_ORDER

        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    def test_accept_courier_wrong_order_id_error(self):
        courier_data = {
            'login': Data.COURIER['login'],
            'password': Data.COURIER['password']
        }

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == 200
        courier_id = response.json()['id']
    
        url = Urls.get_accept_order_url(courier_id, 13)
        response = requests.put(url)
        response_sample = Responses.ACCEPT_ORDER_WRONG_ID_ORDER

        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']
