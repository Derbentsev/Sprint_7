import requests
import allure
from faker import Faker

from data.urls import Urls


class Helpers:

    @allure.step('Создаем фейковые данные по курьеру')
    def create_new_courier_data():
        faker = Faker()
        login = faker.user_name()
        password = faker.password()
        first_name = faker.first_name()

        courier_data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return courier_data


    @allure.step('Отправляем запрос на создание заказа')
    def create_order(payload):
        url = Urls.CREATE_ORDER_URL
        response = requests.post(url, json=payload)
        return response


    @allure.step('Отправляем запрос на создание курьера')
    def create_courier(payload):
        url = Urls.CREATE_COURIER_URL        
        response = requests.post(url, json=payload)
        return response


    @allure.step('Отправляем запрос на авторизацию курьера')
    def authorize_courier(courier_data):
        url = Urls.AUTH_COURIER_URL
        response = requests.post(url, json=courier_data)
        return response
