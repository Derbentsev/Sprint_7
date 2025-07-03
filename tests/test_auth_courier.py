import pytest

from data.data import Data
from data.responses import Responses
from helpers.helpers import Helpers


class TestAuthCourier:

    def test_authorize_courier_success(self):
        payload = Helpers.create_new_courer_data()
        response = Helpers.create_courier(payload)
        assert response.status_code == 201
    
        payload = {
            'login': Data.COURIER['login'],
            'password': Data.COURIER['password']
        }

        response = Helpers.authorize_courier(payload)
        assert response.status_code == 200
        assert 'id' in response.json()


    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def test_authorize_courier_pass_wrong_field_error(self, wrong_field):
        response_sample = Responses.AUTH_COURIER_WRONG_FIELD

        payload = {
            'login': Data.COURIER['login'],
            'password': Data.COURIER['password']
        }

        payload[wrong_field] = payload['login'] + 'test'

        response = Helpers.authorize_courier(payload)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    @pytest.mark.parametrize('no_field', ['login', 'password'])
    def test_authorize_courier_pass_no_field_error(self, no_field):
        response_sample = Responses.AUTH_COURIER_NO_FIELD

        payload = {
            'login': Data.COURIER['login'],
            'password': Data.COURIER['password']
        }

        del payload[no_field]

        response = Helpers.authorize_courier(payload)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_authorize_courier_pass_empty_field_error(self, empty_field):
        response_sample = Responses.AUTH_COURIER_NO_FIELD

        payload = {
            'login': Data.COURIER['login'],
            'password': Data.COURIER['password']
        }

        payload[empty_field] = ''

        response = Helpers.authorize_courier(payload)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']
