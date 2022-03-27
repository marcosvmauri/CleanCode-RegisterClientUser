from faker import Faker
from src.domain.user_cases.test import RegisterClientSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import ClientRepositorySpy, UserRepositorySpy
from .register_client_controller import RegisterClientController

faker = Faker()


def test_route():
    """ Testing route method in RegisterUserRouter """

    register_client_use_case = RegisterClientSpy(ClientRepositorySpy(), UserRepositorySpy())
    register_client_router = RegisterClientController(register_client_use_case)
    attributes = {
        "name": faker.word(),
        "user_id": faker.random_number()
    }

    response = register_client_router.route(HttpRequest(body=attributes))

    assert register_client_use_case.registry_param["name"] == attributes["name"]
    assert register_client_use_case.registry_param["user_id"] == attributes["user_id"]

    assert response.status_code == 200
    assert "error" not in response.body

def test_route_error_no_body():
    """ Testing route method in RegisterUserRouter """

    register_client_use_case = RegisterClientSpy(ClientRepositorySpy(), UserRepositorySpy())
    register_client_router = RegisterClientController(register_client_use_case)

    response = register_client_router.route(HttpRequest())

    assert register_client_use_case.registry_param == {}

    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_wrong_body():
    """ Testing route method in RegisterUserRouter """

    register_client_use_case = RegisterClientSpy(ClientRepositorySpy(), UserRepositorySpy())
    register_client_router = RegisterClientController(register_client_use_case)

    attributes = {
        "user_id": faker.random_number()
    }

    response = register_client_router.route(HttpRequest(body=attributes))

    assert register_client_use_case.registry_param == {}

    assert response.status_code == 422
    assert "error" in response.body


def test_route_error_wrong_user_information():
    """ Testing route method in RegisterUserRouter """

    register_client_use_case = RegisterClientSpy(ClientRepositorySpy(), UserRepositorySpy())
    register_client_router = RegisterClientController(register_client_use_case)

    attributes = {"name": faker.word()}

    response = register_client_router.route(HttpRequest(body=attributes))

    assert register_client_use_case.registry_param == {}

    assert response.status_code == 422
    assert "error" in response.body