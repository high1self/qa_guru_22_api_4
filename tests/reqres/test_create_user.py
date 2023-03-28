from pytest_voluptuous import S

from schemas.user import add_user


def test_create_user_ok(reqres):
    body = {
        "name": "Alex",
        "job": "lead"
    }
    response = reqres.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
    assert response.json()["name"] == "Alex"
    assert response.json()["job"] == "lead"


def test_create_user_without_job(reqres):
    body = {
        "name": "Alex"
    }
    response = reqres.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
