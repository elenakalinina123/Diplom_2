from http import HTTPStatus

import allure
import pytest

from ..data import (empty_ingredients, invalid_id_string, invalid_ingredients,
                    no_ingredient_string, success_string, valid_ingredients)
from ..utils import create_new_order, get_token


class TestOrderCreation:
    @pytest.mark.parametrize(
        'test_case',
        [(empty_ingredients, HTTPStatus.BAD_REQUEST, no_ingredient_string),
         (valid_ingredients, HTTPStatus.OK, success_string),
         (invalid_ingredients, HTTPStatus.BAD_REQUEST, invalid_id_string)]
    )
    @allure.title('Тест на создание заказа для пользователя')
    def test_order_authorized(self, test_case):
        ingredients_json, expected_status, expected_string = test_case
        token = get_token()
        response = create_new_order(ingredients_json, token)

        print(response.text)

        assert response.status_code == expected_status
        assert expected_string in response.text

    @pytest.mark.parametrize(
        'test_case',
        [(empty_ingredients, HTTPStatus.BAD_REQUEST, no_ingredient_string),
         (valid_ingredients, HTTPStatus.OK, success_string),
         (invalid_ingredients, HTTPStatus.BAD_REQUEST, invalid_id_string)]
    )
    @allure.title('Тест на создание заказа для гостя')
    def test_order_unauthorized(self, test_case):
        ingredients_json, expected_status, expected_string = test_case
        response = create_new_order(ingredients_json)
        assert response.status_code == expected_status
        assert expected_string in response.text
