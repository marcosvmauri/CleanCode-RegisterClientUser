from src.domain.models.users import Users
from src.infra.config.db_config import DBConnectionHandler
from .user_repository import UsersRepository
from faker import Faker


faker = Faker();
user_repository = UsersRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_user():
    """Test Insert User """
    try:
        
        name = faker.name()
        password = faker.password()
        engine = db_connection_handler.get_engine()
        
        new_user = user_repository.insert(name, password)
        
        query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
         ).fetchone()
        
    except :
        raise
    
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
    
def test_select_user():
    """Test Select User"""
    
    id = faker.random_number(digits=5)
    name = faker.name()
    password =  faker.password()
    data = Users(id=id, name=name, password=password)
    
    engine = db_connection_handler.get_engine()
    engine.execute(
        "INSERT INTO users (id, name, password) VALUES ('{}','{}','{}');".format(
            id, name, password
        )
    )
    
    query_user1 = user_repository.select(user_id=id)
    query_user2 = user_repository.select(name=name)
    query_user3 = user_repository.select(user_id=id, name=name)
    
    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    engine.execute("DELETE FROM users WHERE id='{}';".format(id))