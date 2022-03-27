from typing import List
from src.domain.models.clients import Clients
from src.domain.test import mock_client


class ClientRepositorySpy:
    """Spy to User Repository"""
    
    def __init__(self):
        self.insert_client_parmas = {}
        self.select_client_parmas = {}
        
    def insert(self, name:str, user_id: int) -> Clients:
        """Spy to all the atributes"""
        
        self.insert_client_parmas["name"] = name
        self.insert_client_parmas["user_id"] = user_id
        
        return mock_client();
 
    def select(self, client_id = None, name = None, user_id : int = None) -> List[Clients]:
        """Spy to all the atributes"""
        
        self.select_client_parmas["client_id"] = client_id
        self.select_client_parmas["name"] = name
        self.select_client_parmas["user_id"] = user_id
        
        return [mock_client()]