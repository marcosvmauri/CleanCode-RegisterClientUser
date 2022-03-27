from faker import Faker
from src.domain.user_cases.test import FindClientSpy
from src.infra.test import ClientRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_client_controller import FindClientController

faker = Faker()


def test_name():
    """ Testing route method in FindClientController """

    find_client_use_case = FindClientSpy(ClientRepositorySpy())
    find_client_router = FindClientController(find_client_use_case)
    attributes = {"name": faker.word()}

    http_request = HttpRequest(query=attributes)
    http_response = find_client_router.route(http_request)
    
    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_by_client_id():
    """ Testing route method in FindClientController """

    find_client_use_case = FindClientSpy(ClientRepositorySpy())
    find_client_router = FindClientController(find_client_use_case)
    attributes = {"client_id": faker.random_number(digits=2)}

    http_request = HttpRequest(query=attributes)
    http_response = find_client_router.route(http_request)

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_by_user_id():
    """ Testing route method in FindClientController """

    find_client_use_case = FindClientSpy(ClientRepositorySpy())
    find_client_router = FindClientController(find_client_use_case)
    attributes = {"user_id": faker.random_number(digits=2)}

    http_request = HttpRequest(query=attributes)

    http_response = find_client_router.route(http_request)

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_error_no_query():
    """ Testing route method in FindClientController """

    find_client_use_case = FindClientSpy(ClientRepositorySpy())
    find_client_router = FindClientController(find_client_use_case)

    http_request = HttpRequest()

    http_response = find_client_router.route(http_request)

    assert http_response.status_code == 400
    assert "error" in http_response.body


def test_route_error_wrong_query():
    """ Testing route method in FindClientController """

    find_client_use_case = FindClientSpy(ClientRepositorySpy())
    find_client_router = FindClientController(find_client_use_case)

    http_request = HttpRequest(query={"something": faker.random_number(digits=2)})

    http_response = find_client_router.route(http_request)

    assert http_response.status_code == 422
    assert "error" in http_response.body