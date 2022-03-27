from faker import Faker
from src.domain.user_cases.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController


faker = Faker()


def test_handle():
    """ Testing Handle method """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(
        query={"user_name": faker.word()}
    )

    response = find_user_controller.route(http_request)

    assert response.status_code == 200
    assert response.body
    

def test_handle_no_query_param():
    """ Testing Handle method """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.route(http_request)

    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    assert "error" in response.body