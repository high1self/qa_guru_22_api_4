from pytest_voluptuous import S

from schemas.user import update_user


def test_update_info_about_user_ok(reqres):
    body = {
        "name": "Alex",
        "job": "lead"
    }
    response = reqres.patch('/api/users/2', data=body)
    assert response.status_code == 200
    assert S(update_user) == response.json()
    assert response.json()["name"] == "Alex"
    assert response.json()["job"] == "lead"


def test_update_info_about_user_when_two_user_job(reqres):
    body = {
        "name": "Alex",
        "job": ["lead", "consalt"]
    }
    response = reqres.patch('/api/users/2', data=body)
    assert response.status_code == 200
    assert response.json()["job"] == ["lead", "consalt"]
