import requests
import pytest

from helpers.helpers import Helpers
from data.urls import Urls
from data.responses import Responses


class TestCreateCourier:

    def test_create_courier_success(self):
        payload = Helpers.create_new_courer_data()
        url = Urls.CREATE_COURIER_URL
        

        response = requests.post(url, data=payload)
        assert response.status_code == 201
        assert response.json() == Responses.CREATE_COURIER_SUCCESS


    def test_create_courier_identical_id_error(self):
        payload = Helpers.create_new_courer_data()
        url = Urls.CREATE_COURIER_URL
        response_sample = Responses.CREATE_COURIER_IDENTICAL_ID

        response = requests.post(url, data=payload)
        assert response.status_code == 201
        
        response = requests.post(url, data=payload)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_create_courier_with_no_fild_error(self, empty_field):
        payload = Helpers.create_new_courer_data()
        url = Urls.CREATE_COURIER_URL
        response_sample = Responses.CREATE_COURIER_NO_FIELD

        del payload[empty_field]

        response = requests.post(url, data=payload)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']
