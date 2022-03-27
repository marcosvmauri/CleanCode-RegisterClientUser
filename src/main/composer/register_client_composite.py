from src.main.interface import RouteInterface
from src.domain.user_cases.register_client import RegisterClient
from src.infra.repo.repositories.client_repository import ClientRepository
from src.presenters.controllers import RegisterClientController

def register_client_composer()-> RouteInterface:
    """Composing Register Clientr RouteInterface
    param - None
    return - Object with Register Client Route"""
    
    repository = ClientRepository()
    use_case = RegisterClient(repository)
    register_client_route = RegisterClientController(use_case)
    
    return register_client_route