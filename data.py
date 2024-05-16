EMAIL = 'email'
NAME = 'name'

api_link = 'https://stellarburgers.nomoreparties.site/api'

ingredients_link = api_link + '/ingredients'
orders_link = api_link + '/orders'
all_orders_link = orders_link + '/all'

password_reset_link = api_link + '/password-reset'
reset_password_link = api_link + '/reset-password'
reset_reset_link = reset_password_link + '/reset'

auth_link = api_link + '/auth'
register_link = auth_link + '/register'
login_link = auth_link + '/login'
logout_link = auth_link + '/logout'
token_refresh_link = auth_link + '/token'
user_info_link = auth_link + '/user'

success_string = '"success":true,'
success_false_string = '"success":false,'
failed_registration_string = '"success":false,"message":"User already exists"'
missing_field_error = '"success":false,"message":"Email, password and name are required fields"'
failed_login_string = '"success":false,"message":"email or password are incorrect"'
unauthorised_string = '"message":"You should be authorised"'
invalid_id_string = 'One or more ids provided are incorrect'
no_ingredient_string = 'Ingredient ids must be provided'

empty_ingredients = {'ingredients': ''}
invalid_ingredients = {'ingredients': [
    "60d3b41abdacab0026a733c7", "609646e4dc916e00276b2871"]}
valid_ingredients = {'ingredients': ["61c0c5a71d1f82001bdaaa74",
                     "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]}
