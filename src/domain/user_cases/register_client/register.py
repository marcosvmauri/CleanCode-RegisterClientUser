from typing import Type, Dict
from src.domain.models import Clients
from src.domain.user_cases.interfaces import RegisterClient as RegisterClientInterface
from src.infra.repo.interfaces.client_repository_interface import ClientRepositoryInterface

class RegisterClient(RegisterClientInterface):
    """Class to define user case Register User"""
    
    def __init__(self, client_repository: Type[ClientRepositoryInterface]):
        self.client_repository = client_repository
        
    def register(self, name: str, user_id: int) -> Dict[bool, Clients]:
        """Register client case
        :param  - name: The name of the client
                - user_id: id of the user
        :return - Dictionary with information of the process"""
        
        response = None
        validate_client = isinstance(name, str) and isinstance(user_id, int)
       
        if validate_client:
            response = self.client_repository.insert(name, user_id)
            
        return {"Success": validate_client, "Data": response}
        