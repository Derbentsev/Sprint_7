import requests
import pytest

from helpers.helpers import Helpers
from urls.urls import Urls
from data.data import Data


class TestAuthCourier:

    def authorize_courier_success():
        courier_data = Data.COURIER
        url = Urls.AUTH_COURIER_URL()

        payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        response = requests.post(url, payload)
        assert response.status_code == 200
        assert response.json() == 'id'


    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def authorize_courier_pass_wrong_field_error(wrong_field):
        courier_data = Data.COURIER
        url = Urls.AUTH_COURIER_URL()

        payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        payload[wrong_field] = payload['login'] + 'test'

        response = requests.post(url, payload)
        assert response.status_code == 400


    @pytest.mark.parametrize('no_field', ['login', 'password'])
    def authorize_courier_pass_wrong_field_error(no_field):
        courier_data = Data.COURIER
        url = Urls.AUTH_COURIER_URL()

        payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        del payload[no_field]

        response = requests.post(url, payload)
        assert response.status_code == 400
