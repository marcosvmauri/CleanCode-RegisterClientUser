from src.main.interface import RouteInterface
from src.domain.user_cases.find_client import FindClient
from src.presenters.controllers import FindClientController
from src.infra.repo.repositories.client_repository import ClientRepository

def find_client_composer()-> RouteInterface:
    """Composing Find Clientr RouteInterface
    param - None
    return - Object with Find Client Route"""
    
    repository = ClientRepository()
    use_case = FindClient(repository)
    register_client_route = FindClientController(use_case)
    
    return register_client_route