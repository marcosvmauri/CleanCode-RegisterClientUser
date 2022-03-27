from src.domain.models.clients import Clients
from src.infra.config.db_config import DBConnectionHandler
from faker import Faker
from src.infra.repo.repositories.client_repository import ClientRepository


faker = Faker();
client_repository = ClientRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_client():
    """Test Insert Client """
    try:
        
        name = faker.name()
        id_User = faker.random_number(digits=5)
        engine = db_connection_handler.get_engine()
        
        new_client = client_repository.insert(name, id_User)
        
        query_client = engine.execute(
        "SELECT * FROM clients WHERE id='{}';".format(new_client.id)
         ).fetchone()
        
    except :
        raise
    
    assert new_client.id == query_client.id
    assert new_client.name == query_client.name
    
def test_select_client():
    """Test Select Client"""
    
    id = faker.random_number(digits=5)
    name = faker.name()
    password =  faker.password()
    user_id = faker.random_number(digits=5)
    data = Clients(id=id, name=name, user_id=user_id)
    
    engine = db_connection_handler.get_engine()
    engine.execute(
        "INSERT INTO clients (id, name, user_id) VALUES ('{}','{}','{}');".format(
            id, name, user_id
        )
    )
    
    query_client1 = client_repository.select(client_id=id)
    query_client2 = client_repository.select(name=name)
    query_client3 = client_repository.select(client_id=id, name=name)
    
    assert data in query_client1
    assert data in query_client2
    assert data in query_client3

    engine.execute("DELETE FROM clients WHERE id='{}';".format(id))