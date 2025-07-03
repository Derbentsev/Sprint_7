import requests
from faker import Faker

from data.urls import Urls


class Helpers:

    @staticmethod
    def create_new_courer_data():
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


    @staticmethod
    def create_order(payload):
        url = Urls.CREATE_ORDER_URL
        response = requests.post(url, payload)
        return response


    @staticmethod
    def create_courier(payload):
        url = Urls.CREATE_COURIER_URL        
        response = requests.post(url, payload)
        return response


    @staticmethod
    def authorize_courier(payload):
        url = Urls.AUTH_COURIER_URL   
        response = requests.post(url, payload)
        return response
