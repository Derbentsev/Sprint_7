import requests
import pytest

from helpers.helpers import Helpers
from urls.urls import Urls


class TestCreateCourier:

    def test_create_courier_success(self):
        payload = Helpers.create_new_courer_data()
        url = Urls.CREATE_COURIER_URL
        print(payload)

        response = requests.post(url, data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}


    def test_create_identical_courier_unsuccess(self):
        payload = Helpers.create_new_courer_data()
        url = Urls.CREATE_COURIER_URL

        response = requests.post(url, data=payload)
        assert response.status_code == 201
        
        response = requests.post(url, data=payload)
        assert response.status_code == 409


    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_create_courier_with_no_required_fild_unsuccess(self, empty_field):
        payload = Helpers.create_new_courer_data()
        url = Urls.CREATE_COURIER_URL

        del payload[empty_field]

        response = requests.post(url, data=payload)
        assert response.status_code == 400
