class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    CREATE_COURIER_URL = f'{MAIN_URL}/courier'
    AUTH_COURIER_URL = f'{MAIN_URL}/courier/login'
    CREATE_ORDER_URL = f'{MAIN_URL}/orders'
    GET_ORDER_LIST_URL = f'{MAIN_URL}/orders'
    DEL_COURIER_URL = f'{MAIN_URL}/courier/:id'
    ACCEPT_ORDER_URL = f'{MAIN_URL}/accept/:id'
    GET_ORDER_URL = f'{MAIN_URL}/orders/track'
