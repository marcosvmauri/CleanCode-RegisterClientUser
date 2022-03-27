from faker import Faker
from src.infra.test import ClientRepositorySpy
from .find import FindClient

faker = Faker()


def test_by_id():
    """ Testing by_id method in FindClient """

    client_repo = ClientRepositorySpy()
    find_client = FindClient(client_repo)

    attribute = {"id": faker.random_number(digits=2)}
    response = find_client.by_id(client_id=attribute["id"])

    assert client_repo.select_client_parmas["client_id"] == attribute["id"]

    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_id():
    """ Testing by_id fail method in FindClient """

    client_repo = ClientRepositorySpy()
    find_client = FindClient(client_repo)

    attribute = {"id": faker.word()}
    response = find_client.by_id(client_id=attribute["id"])

    assert client_repo.select_client_parmas == {}

    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """ Testing by_name method in FindClient """

    client_repo = ClientRepositorySpy()
    find_client = FindClient(client_repo)

    attribute = {"name": faker.word()}
    response = find_client.by_name(name=attribute["name"])

    assert client_repo.select_client_parmas["name"] == attribute["name"]

    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_name():
    """ Testing by_name fail method in FindClient """

    client_repo = ClientRepositorySpy()
    find_client = FindClient(client_repo)

    attribute = {"name": faker.random_number(digits=2)}
    response = find_client.by_name(name=attribute["name"])

    assert client_repo.select_client_parmas == {}

    assert response["Success"] is False
    assert response["Data"] is None