import pytest
import allure

from data.responses import Responses
from helpers.helpers import Helpers


@allure.parent_suite('Авторизация курьера')
class TestAuthCourier:

    @allure.title('Успешная авторизация курьера')
    def test_authorize_courier_success(self):
        courier_data = Helpers.create_new_courier_data()
        response = Helpers.create_courier(courier_data)
        assert response.status_code == 201

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == 200
        assert 'id' in response.json()


    @allure.title('Неуспешная авторизация курьера при некорректных данных')
    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def test_authorize_courier_pass_wrong_field_error(self, wrong_field):
        courier_data = Helpers.create_new_courier_data()
        response = Helpers.create_courier(courier_data)
        assert response.status_code == 201

        response_sample = Responses.AUTH_COURIER_WRONG_FIELD
        courier_data[wrong_field] = courier_data['login'] + 'test'

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    @allure.title('Неуспешная авторизация курьера при отсутствии поля')
    @pytest.mark.parametrize('no_field', ['login', 'password'])
    def test_authorize_courier_pass_no_field_error(self, no_field, courier_data):
        response_sample = Responses.AUTH_COURIER_NO_FIELD

        del courier_data[no_field]

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']


    @allure.title('Неуспешная авторизация курьера при незаполненном поле')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_authorize_courier_pass_empty_field_error(self, empty_field, courier_data):
        response_sample = Responses.AUTH_COURIER_NO_FIELD

        courier_data[empty_field] = ''

        response = Helpers.authorize_courier(courier_data)
        assert response.status_code == response_sample['code']
        assert response.json()['message'] == response_sample['message']
