import pytest
import allure

from data.data import Data
from helpers.helpers import Helpers


@allure.parent_suite('Создание заказа')
class TestCreateOrder:
    
    @allure.title('Успешное создание заказа')
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK', 'GREY'],
            ['BLACK'],
            ['GREY'],
            ['']
        ]
    )
    def test_create_order_success(self, color):
        payload = Data.ORDER
        payload['color'] = color

        response = Helpers.create_order(payload)
        assert response.status_code == 201
        assert 'track' in response.json()
