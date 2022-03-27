from collections import UserString
from faker import Faker
from src.domain.models.clients import Clients



faker = Faker()

def mock_client() -> Clients:
    """Mock Users"""
    
    return Clients(
        id=faker.random_number(digits=5), name=faker.name(), user_id=faker.random_number(digits=5)
    )