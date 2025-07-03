import requests
import pytest

from data.urls import Urls


class TestOrderList:
    
    @pytest.mark.parametrize('params', 
    [
        {'limit': 10, 'page': 0},
        {'nearestStation': ['1'], 'limit': 10, 'page': 0},
        {'courierId': 1, 'limit': 10, 'page': 0}
    ])
    def test_get_orsers_list_success(self, params):
        url = Urls.GET_ORDER_LIST_URL

        response = requests.get(url, params=params)
        assert response.status_code == 200
        assert 'orders' in response.json()
