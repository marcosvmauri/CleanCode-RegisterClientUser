from faker import Faker
from src.domain.user_cases.interfaces.register_client import RegisterClient
from src.infra.test.client_repository_spy import ClientRepositorySpy
from .register import RegisterClient

faker = Faker()

def test_register():
    """Teste register method"""
    
    client_repo = ClientRepositorySpy()
    register_client = RegisterClient(client_repo)
    
    attributes ={
        "name": faker.name(),
        "password": faker.password(),
        "user_id" : faker.random_number(digits=5)
    }
    response = register_client.register(name=attributes["name"], user_id=attributes["user_id"] )
    
    assert client_repo.insert_client_parmas["name"] == attributes["name"]
    assert client_repo.insert_client_parmas["user_id"] == attributes["user_id"]
    
    assert response["Sucess"] is True
    assert response["Data"]