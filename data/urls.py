class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    CREATE_COURIER_URL = f'{MAIN_URL}/courier'
    AUTH_COURIER_URL = f'{MAIN_URL}/courier/login'
    CREATE_ORDER_URL = f'{MAIN_URL}/orders'
    GET_ORDER_LIST_URL = f'{MAIN_URL}/orders'
    DEL_COURIER_URL = f'{MAIN_URL}/courier'
    ACCEPT_ORDER_URL = f'{MAIN_URL}/orders/accept/1'
    GET_ORDER_URL = f'{MAIN_URL}/orders/track'


    @staticmethod
    def get_del_courier_url(courier_id):
        return f'{Urls.DEL_COURIER_URL}/{courier_id}'


    @staticmethod
    def get_accept_order_url(courier_id, order_id):
        return f'{Urls.ACCEPT_ORDER_URL}?{order_id}&courierId={courier_id}'
