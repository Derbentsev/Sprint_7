class Responses:
    DEL_COURIER_SUCCESS = {'ok': True}
    DEL_COURIER_NO_ID = {'code': 400, 'message': 'Недостаточно данных для удаления курьера'}
    DEL_COURIER_NO_EXISTS_ID = {'code': 404, 'message': 'Курьера с таким id нет.'}

    AUTH_COURIER_WRONG_FIELD = {'code': 404, 'message': 'Учетная запись не найдена'}
    AUTH_COURIER_NO_FIELD = {'code': 400, 'message': 'Недостаточно данных для входа'}

    CREATE_COURIER_SUCCESS = {'ok': True}
    CREATE_COURIER_IDENTICAL_ID = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    CREATE_COURIER_NO_FIELD = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    ACCEPT_ORDER_SUCCESS = {'ok': True}
    ACCEPT_ORDER_NO_ID_ORDER = {'code': 400, 'message': 'Недостаточно данных для поиска'}
    ACCEPT_ORDER_WRONG_ID_ORDER = {'code': 404, 'message': 'Заказа с таким id не существует'}
    ACCEPT_ORDER_NO_ID_COURIER = {'code': 400, 'message': 'Недостаточно данных для поиска'}
    ACCEPT_ORDER_WRONG_ID_COURIER = {'code': 404, 'message': 'Курьера с таким id не существует'}

    GET_ORDER_NO_ID = {'code': 400, 'message': 'Недостаточно данных для поиска'}
    GET_ORDER_WRONG_ID = {'code': 404, 'message': 'Заказ не найден'}
