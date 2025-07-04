import pytest
import allure

from helpers.helpers import Helpers
from data.responses import Responses


@allure.parent_suite('Созданеи курьера')
class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self):
        payload = Helpers.create_new_courier_data()

        response = Helpers.create_courier(payload)
        assert response.status_code == 201
        assert response.json() == Responses.CREATE_COURIER_SUCCESS


    @allure.title('Неуспешное создание дубля курьера')
    def test_create_courier_identical_id_error(self):
        payload = Helpers.create_new_courier_data()
        response_sample = Responses.CREATE_COURIER_IDENTICAL_ID

        response = Helpers.create_courier(payload)
        assert response.status_code == 201
        
        response = Helpers.create_courier(payload)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    @allure.title('Неуспешное создание курьера при передаче пустого поля')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_create_courier_with_no_fild_error(self, empty_field):
        payload = Helpers.create_new_courier_data()
        response_sample = Responses.CREATE_COURIER_NO_FIELD

        del payload[empty_field]

        response = Helpers.create_courier(payload)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']
