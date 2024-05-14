from http import HTTPStatus

import allure

from ..data import failed_login_string, success_string
from ..utils import generate_user_data, login_user, register_new_user


class TestUserLogin:
    @allure.title('Тест на успешный логин')
    def test_successfull_login(self):
        data = generate_user_data()
        register_new_user(data)
        response = login_user(data)

        assert response.status_code == HTTPStatus.OK
        assert success_string in response.text

    @allure.title('Тест на логин с неверным паролем')
    def test_login_wrong_password(self):
        data = generate_user_data()
        response = login_user(data)

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert failed_login_string in response.text
