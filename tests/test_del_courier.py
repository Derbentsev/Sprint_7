import requests

from data.urls import Urls
from data.responses import Responses
from helpers.helpers import Helpers


class DelCourier:
    def test_del_courier_success(self):
        payload = Helpers.create_new_courer_data()
        response = Helpers.create_courier(payload)
        assert response.status_code == 201
    
        url = Urls.get_del_courier_url(123)

        response = requests.delete(url)
        assert response.status_code == 200
        assert response.json() == Responses.DEL_COURIER_SUCCESS


    def test_del_courier_no_id_success(self):
        url = Urls.DEL_COURIER_URL
        response_sample = Responses.DEL_COURIER_NO_ID

        response = requests.delete(url)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']


    def test_del_courier_no_exists_id_success(self):
        url = Urls.get_del_courier_url(1233232)
        response_sample = Responses.DEL_COURIER_NO_EXISTS_ID

        response = requests.delete(url)
        assert response.status_code == response_sample['code']
        assert response.json() == response_sample['message']
