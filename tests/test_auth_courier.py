import requests
import pytest

from data.urls import Urls
from data.data import Data
from data.responses import Responses


class TestAuthCourier:

    def test_authorize_courier_success(self):
        courier_data = Data.COURIER
        url = Urls.AUTH_COURIER_URL

        payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        response = requests.post(url, payload)
        assert response.status_code == 200
        assert 'id' in response.json()


    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def test_authorize_courier_pass_wrong_field_error(self, wrong_field):
        courier_data = Data.COURIER
        url = Urls.AUTH_COURIER_URL
        response_sample = Responses.AUTH_COURIER_WRONG_FIELD

        payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        payload[wrong_field] = payload['login'] + 'test'

        response = requests.post(url, payload)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    @pytest.mark.parametrize('no_field', ['login', 'password'])
    def test_authorize_courier_pass_no_field_error(self, no_field):
        courier_data = Data.COURIER
        url = Urls.AUTH_COURIER_URL
        response_sample = Responses.AUTH_COURIER_NO_FIELD

        payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        del payload[no_field]

        response = requests.post(url, payload)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_authorize_courier_pass_empty_field_error(self, empty_field):
        courier_data = Data.COURIER
        url = Urls.AUTH_COURIER_URL
        response_sample = Responses.AUTH_COURIER_NO_FIELD

        payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        payload[empty_field] = ''

        response = requests.post(url, payload)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']
