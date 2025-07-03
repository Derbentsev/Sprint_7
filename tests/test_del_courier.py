import requests

from data.urls import Urls
from data.responses import Responses
from helpers.helpers import Helpers


class TestDelCourier:
    def test_del_courier_success(self):
        payload = Helpers.create_new_courier_data()
        response = Helpers.create_courier(payload)
        assert response.status_code == 201
    
        courier_data = {
            'login': payload['login'],
            'password': payload['password']
        }

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == 200
        courier_id = response.json()['id']

        url = Urls.get_del_courier_url(courier_id)

        response = requests.delete(url)
        assert response.status_code == 200
        assert response.json() == Responses.DEL_COURIER_SUCCESS


    def test_del_courier_no_id_error(self):
        url = Urls.DEL_COURIER_URL
        response_sample = Responses.DEL_COURIER_NO_ID

        response = requests.delete(url)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    def test_del_courier_no_exists_id_error(self):
        url = Urls.get_del_courier_url(1233232)
        response_sample = Responses.DEL_COURIER_NO_EXISTS_ID

        response = requests.delete(url)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']
