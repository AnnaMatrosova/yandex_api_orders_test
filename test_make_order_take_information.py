import order_stand_request


# Проверка получения информации о заказе по его трек-номеру
def test_get_success_response():
    info_response = order_stand_request.get_information()
    assert info_response.status_code == 200
