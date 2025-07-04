import requests
import allure

from data.urls import Urls
from helpers.helpers import Helpers


@allure.parent_suite('Получение списка заказов')
class TestOrderList:
    
    @allure.title('Успешное получение списка заказов')
    def test_get_orders_list_success(self):
        courier_data = Helpers.create_new_courier_data()
        response = Helpers.create_courier(courier_data)
        assert response.status_code == 201

        response = Helpers.authorize_courier(courier_data)
        courier_id = response.json()['id']

        params = {
            'courierId': courier_id,
            'nearestStation': ["1"],
            'limit': 10,
            'page': 0
        }

        url = Urls.GET_ORDER_LIST_URL

        response = requests.get(url, params=params)
        assert response.status_code == 200
        assert 'orders' in response.json()
