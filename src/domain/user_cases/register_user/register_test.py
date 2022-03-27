from faker import Faker
from src.infra.test.user_repository_spy import UserRepositorySpy
from .register import RegisterUser

faker = Faker()

def test_register():
    """Teste register method"""
    
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)
    
    attributes ={
        "name": faker.name(),
        "password": faker.password(),
    }
    response = register_user.register(name=attributes["name"], password=attributes["password"])
    
    assert user_repo.insert_user_parmas["name"] == attributes["name"]
    assert user_repo.insert_user_parmas["password"] == attributes["password"]
    
    assert response["Sucess"] is True
    assert response["Data"]