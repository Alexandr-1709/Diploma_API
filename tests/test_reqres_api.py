import json

from allure import step
from models.helper import reqres_session, validate_shema
from models.page import app
from models.data_reqres import *
import allure
from allure_commons.types import Severity


@allure.tag('api')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Nikiforov')
@allure.description('Создание пользователя')
@allure.feature('Проверка создания пользователя, при вводе валидных данных')
def test_create_user():
    pyload = {"name": create_name,
              "job": create_job}
    with allure.step('POST запрос c валидными данными в теле запроса'):
        response = reqres_session.post("/api/users", json=pyload)
    with step('Валидация json схемы ответа'):
        validate_shema(app.created_user, response.json())


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Nikiforov')
@allure.description('Обновление пользователей')
@allure.feature('Проверка обновления name, job пользователя по id')
def test_put_update_user():
    pyload = {"name": name_update,
              "job": job_update}
    with allure.step('POST запрос с валидными данными'):
        response = reqres_session.put(f"/api/users/{id_user_update}", json=pyload)
    with allure.step('Проверка успешного обновления пользователя'):
        assert response.status_code == 200
        assert response.json()['name'] == 'test'
        assert response.json()['job'] == 'engineer'
    with step('Валидация json схемы ответа'):
        validate_shema(app.update_user, response.json())


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Nikiforov')
@allure.description('Удаление пользователей')
@allure.feature('Проверка удаления пользователя')
def test_delete_user():
    with allure.step(f'Отправка запроса DELETE с id {user_id_delete}'):
        response = reqres_session.delete(f"/api/users/{user_id_delete}")
    with allure.step('Проверка статус-кода ответа'):
        assert response.status_code == 204
        assert response.headers['Content-Length'] == '0'


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Nikiforov')
@allure.description('Авторизация пользователя')
@allure.feature('Проверка авторизации пользователя с валидными данными')
def test_login_successful():
    pyload = {"email": login_email,
              "password": login_password}

    response = reqres_session.post('/api/login', json=pyload)
    with allure.step('Проверка статус-кода ответа и получение токена'):
        assert response.status_code == 200
        assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'
    with step('Валидация json схемы ответа'):
        validate_shema(app.login_successful, response.json())


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Nikiforov')
@allure.description('Регистрация без пароля')
@allure.feature('Проверка ошибки авторизации пользователя без передачи пароля в теле запроса')
def test_login_unsuccessful():
    pyload = {"email": "eve.holt@reqres.in"}
    with allure.step('POST запрос без обязательного параметра password'):
        response = reqres_session.post('/api/login', json=pyload)
    with allure.step('Проверка статус-кода и ошибки в ответе'):
        assert response.status_code == 400
        assert response.json()['error'] == 'Missing password'
    with step('Валидация json схемы ответа'):
        validate_shema(app.unsuccessful_register, response.json())


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Nikiforov')
@allure.description('Пользователь по id')
@allure.feature(f'Проверка возвращения в ответе пользователя по заданному id {id_user}')
def test_get_single():
    with step(f'GET запрос c id пользователя'):
        response = reqres_session.get(f'/api/users/{id_user}')
    with step(f'Проверка получения в ответе данных пользователя с id {id_user}'):
        assert response.status_code == 200
        assert response.json()['data']['id'] == 6
        assert response.json()['data']['email'] == 'tracey.ramos@reqres.in'
        assert response.json()['data']['first_name'] == 'Tracey'
        assert response.json()['data']['last_name'] == 'Ramos'

    with step('Валидация json схемы ответа'):
        validate_shema(app.get_single_user, response.json())



@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Nikiforov')
@allure.description('Список ресурсов')
@allure.feature(f'Проверка метода, возврвщающего список источников')
def test_get_list_resources():
    with step(f'GET запрос c необозначенным источником'):
        response = reqres_session.get('/api/unknown')
    with step('Проверка статус-кода и общего количества источников в списке (12)'):
        assert response.status_code == 200
        assert response.json()['total'] == 12
    with step('Валидация json схемы ответа'):
        validate_shema(app.get_list_resourses_shema, response.json())
