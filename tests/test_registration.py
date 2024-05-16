from http import HTTPStatus

import allure
import pytest

from ..data import (failed_registration_string, missing_field_error,
                    success_string)
from ..utils import generate_user_data, register_new_user


class TestUserRegistration:
    @allure.title('Тест успешной регистрации пользователя')
    def test_succesfull_user_creation(self):
        data = generate_user_data()
        response = register_new_user(data)
        assert response.status_code == HTTPStatus.OK
        assert success_string in response.text

    @allure.title('Тест на регистрацию двух одинаковых пользователей')
    def test_failed_duplicate_user_creation(self):
        data = generate_user_data()
        register_new_user(data)
        response = register_new_user(data)
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert failed_registration_string in response.text

    @allure.title('Тест на проваленную регистрацию из-за отсутствия поля')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_failed_user_creation_missing_field(self, missing_field):
        data = generate_user_data()
        data[missing_field] = ''
        response = register_new_user(data)

        assert response.status_code == HTTPStatus.FORBIDDEN
        assert missing_field_error in response.text
