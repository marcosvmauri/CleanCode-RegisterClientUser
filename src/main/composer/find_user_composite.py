from src.main.interface import RouteInterface
from src.domain.user_cases.find_user import FindUser
from src.presenters.controllers import FindUserController
from src.infra.repo.repositories.user_repository import UsersRepository

def find_user_composer()-> RouteInterface:
    """Composing Find Userr RouteInterface
    param - None
    return - Object with Find User Route"""
    
    repository = UsersRepository()
    use_case = FindUser(repository)
    register_user_route = FindUserController(use_case)
    
    return register_user_route