from http import HTTPStatus

import allure
import pytest

from ..data import (EMAIL, NAME, success_false_string, success_string,
                    unauthorised_string)
from ..utils import (generate_user_data, login_user, patch_user_data,
                     register_new_user)


class TestPatchUser:
    @allure.title('Тест на успешное изменение информации пользователя')
    @pytest.mark.parametrize('data_key', ['email', 'name'])
    def test_patch_user_logged_in(self, data_key):
        data = generate_user_data()
        register_new_user(data)
        response = login_user(data)

        token = response.json()['accessToken']
        response, data = patch_user_data(data, token, data_key)

        assert response.status_code == HTTPStatus.OK
        assert success_string in response.text
        assert data[EMAIL] and data[NAME] in response.text

    @allure.title('Тест на успешное изменение информации пользователя')
    @pytest.mark.parametrize('data_key', ['email', 'name'])
    def test_patch_user_unauthorised(self, data_key):
        data = generate_user_data()

        response, data = patch_user_data(data, '', data_key)

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert success_false_string and unauthorised_string in response.text
