from http import HTTPStatus

import allure
import pytest

from ..data import success_false_string, success_string
from ..utils import get_token, get_user_orders_list


class TestGetUserOrders:
    @allure.title('Тест на получение списка заказов аутентифицированного пользователя')  # noqa
    @pytest.mark.parametrize(
        'test_case',
        [(True, HTTPStatus.OK, success_string),
         (False, HTTPStatus.UNAUTHORIZED, success_false_string)])
    def test_get_user_orders(self, test_case):
        token = ''
        is_authorised, expected_status, expected_string = test_case

        if is_authorised:
            token = get_token()

        response = get_user_orders_list(token)

        assert response.status_code == expected_status
        assert expected_string in response.text
