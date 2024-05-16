from http import HTTPStatus

import allure

from ..data import success_false_string, success_string
from ..utils import get_token, get_user_orders_list


class TestGetUserOrders:
    @allure.title('Тест на получение списка заказов аутентифицированного пользователя')  # noqa
    def test_get_user_orders_authorized(self, test_case):
        response = get_user_orders_list(get_token())

        assert response.status_code == HTTPStatus.OK
        assert success_string in response.text

    @allure.title('Тест на получение списка заказов аутентифицированного пользователя')  # noqa
    def test_get_user_orders_unauthorized(self):
        response = get_user_orders_list()

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert success_false_string in response.text
