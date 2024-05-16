import random
import string

import allure
import requests

from .data import login_link, orders_link, register_link, user_info_link


@allure.step('генерируем случайную строку')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('генерируем случайные данные пользователя')
def generate_user_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    email = login + '@yandex.ru'

    data = {
        "email": email,
        "password": password,
        "name": name
    }

    return data


@allure.step('регистрируем нового пользователя')
def register_new_user(data):
    return requests.post(register_link, data=data)


@allure.step('авторизовываем пользователя')
def login_user(data):
    return requests.post(login_link, data=data)


@allure.step('изменяем данные пользователя')
def change_user_data(data, data_key):
    data.update({data_key: generate_random_string(11)})
    return data


@allure.step('изменяем данные пользователя')
def patch_user_data(data, token, data_key):
    data = change_user_data(data, data_key)

    headers = {"Authorization": token}
    response = requests.patch(user_info_link, data=data, headers=headers)
    return response, data


@allure.step('получаем токен пользователя')
def get_token():
    data = generate_user_data()
    register_new_user(data)
    response = login_user(data)
    token = response.json()['accessToken']
    return token


@allure.step('создаем новый заказ')
def create_new_order(order_json, token=None):
    kwargs = {}
    if token:
        kwargs.update({'headers': {"Authorization": token}})

    return requests.post(orders_link, json=order_json, **kwargs)


@allure.step('получаем список заказов')
def get_user_orders_list(token=None):
    kwargs = {}
    if token:
        kwargs.update({'headers': {"Authorization": token}})
    return requests.get(orders_link, **kwargs)
