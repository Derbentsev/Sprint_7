import random
import string
from faker import Faker


class Helpers:
    
    @staticmethod
    def create_login_password(self):
        faker = Faker()
        login = faker.user_name
        password = faker.password
        first_name = faker.name

        courier_data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return courier_data
