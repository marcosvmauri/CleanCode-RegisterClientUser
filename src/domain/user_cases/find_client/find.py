from typing import Type, Dict
from src.domain.models import Clients
from src.domain.user_cases.interfaces import FindClient as FindClientInterface
from src.infra.repo.interfaces.client_repository_interface import ClientRepositoryInterface

class FindClient(FindClientInterface):
    """Class to define usercase Register Client"""
    
    def __init__(self, user_repository: Type[ClientRepositoryInterface]):
        self.user_repository = user_repository
        
    def by_id(self,client_id:int) -> Dict[bool, Clients]:
        """Register user case
        :param  - id: The name of the client
        :return - Dictionary with information of the process"""
        
        response = None
        validate_user = isinstance(client_id, int)
        
        if validate_user:
            response = self.user_repository.select(client_id=client_id)
            
        return {"Success": validate_user, "Data": response}
    
    def by_name(self,name:str) -> Dict[bool, Clients]:
        """Register user case
        :param  - id: The name of the client
        :return - Dictionary with information of the process"""
        
        response = None
        validate_user = isinstance(name, str)
        
        if validate_user:
            response = self.user_repository.select(name=name)
            
        return {"Success": validate_user, "Data": response} 
    
    def by_user_id(self,user_id:int) -> Dict[bool, Clients]:
        """Register user case
        :param  - id: The name of the client
        :return - Dictionary with information of the process"""
        
        response = None
        validate_user = isinstance(user_id, int)
        
        if validate_user:
            response = self.user_repository.select(name=user_id)
            
        return {"Success": validate_user, "Data": response} 
        