import configuration
import requests
import data


# Создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.MAKE_ORDER_PATH,
                         json=data.orders_body)
Track = post_new_order().json()['track'] # Coхранение трекера нового заказа

# Получить данные о заказе
def get_information():
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_INFORMATION_PATH,
                        params={"t": Track})







