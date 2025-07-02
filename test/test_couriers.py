import requests
import pytest

from helpers.helpers import Helpers
from data.urls import Urls
from data.data import Data


class TestCourier:
    
    def test_create_courier_success():
        payload = Helpers.create_login_password()
        url = Urls.CREATE_COURIER_URL()

        response = requests.post(url, data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}


    def test_create_identical_courier_unsuccess():
        payload = Helpers.create_login_password()
        url = Urls.CREATE_COURIER_URL()

        response = requests.post(url, data=payload)
        if response.status_code != 201:
            assert False
            
        response = requests.post(url, data=payload)
        assert response.status_code == 400


    @pytest.mark.parametrize('empty_field', ['login', 'password', 'firstName'])
    def test_create_courier_with_no_required_fild_unsuccess(empty_field):
        payload = Helpers.create_login_password()
        url = Urls.CREATE_COURIER_URL()

        del payload[empty_field]

        response = requests.post(url, data=payload)
        assert response.status_code == 400
