import requests
import allure

from data.urls import Urls
from data.responses import Responses
from helpers.helpers import Helpers


@allure.parent_suite('Удаление курьера')
class TestDelCourier:
    @allure.title('Успешное удаление курьера')
    def test_del_courier_success(self):
        courier_data = Helpers.create_new_courier_data()
        response = Helpers.create_courier(courier_data)
        assert response.status_code == 201

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == 200
        courier_id = response.json()['id']

        url = Urls.get_del_courier_url(courier_id)

        response = requests.delete(url)
        assert response.status_code == 200
        assert response.json() == Responses.DEL_COURIER_SUCCESS


    @allure.title('Ошибка при удалении курьера без id курьера')
    def test_del_courier_no_id_error(self):
        url = Urls.DEL_COURIER_URL
        response_sample = Responses.DEL_COURIER_NO_ID

        response = requests.delete(url)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    @allure.title('Ошибка удаления курьера при передаче '\
                  'несуществующего id курьера')
    def test_del_courier_no_exists_id_error(self):
        url = Urls.get_del_courier_url(1233232)
        response_sample = Responses.DEL_COURIER_NO_EXISTS_ID

        response = requests.delete(url)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']
