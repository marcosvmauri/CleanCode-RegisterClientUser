from src.main.interface import RouteInterface
from src.domain.user_cases.register_user import RegisterUser
from src.infra.repo.repositories.user_repository import UsersRepository
from src.presenters.controllers import RegisterUserController

def register_user_composer()-> RouteInterface:
    """Composing Register Userr RouteInterface
    param - None
    return - Object with Register User Route"""
    
    repository = UsersRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)
    
    return register_user_route