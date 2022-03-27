from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Clients

class ClientRepositoryInterface(ABC):
    """Interface to User Repository"""
    
    @abstractmethod
    def insert(self, name: str, user_id: int)-> Clients:
        """Client user"""
        
        raise Exception("Method not implemented")
    
    @abstractmethod
    def select(self, client_id: int = None, name: str = None)-> List[Clients]:
        """select client"""
        
        raise Exception("Method not implemented")