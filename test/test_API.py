import requests
from jsonschema import validate
from test.schemas import *


def test_get_single_resource():
    response = requests.get("https://reqres.in/api/unknown/2")
    body = response.json()
    validate(body, schema_get_single_resource)

    assert response.status_code == 200


def test_get_single_resource_not_found():
    response = requests.get("https://reqres.in/api/unknown/23")

    assert response.status_code == 404
    assert response.text == '{}'


def test_post_create_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post("https://reqres.in/api/users", data=data)
    body = response.json()
    validate(body, schema_create_user)

    assert response.status_code == 201


def test_put_update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put("https://reqres.in/api/users/2", data=data)
    body = response.json()
    validate(body, schema_update_user)

    assert response.status_code == 200


def test_patch_update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.patch("https://reqres.in/api/users/2", data=data)
    body = response.json()
    validate(body, schema_update_user)

    assert response.status_code == 200


def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2")

    assert response.status_code == 204
    assert response.text == ""


def test_delete_user_negative():
    response = requests.delete("https://reqres.in/api/users/23754")

    assert response.status_code == 404


def test_post_unsuccessful_login():
    data = {
        "email": "peter@klaven"
    }
    response = requests.post("https://reqres.in/api/login", data=data)
    body = response.json()
    validate(body, schema_post_unsuccessful_login)

    assert response.status_code == 400
    assert body['error'] == "Missing password"
