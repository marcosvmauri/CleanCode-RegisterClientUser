from typing import Dict, List
from abc import ABC, abstractclassmethod
from src.domain.models import Clients

class FindClient(ABC):
    """Interface User Case to Find Clinet"""
    
    @abstractclassmethod
    def by_id(cls, client_id: int)-> Dict[bool, List[Clients]]:
        """Find by id """
        
        raise Exception("Should implement method: by_id")
    
    @abstractclassmethod
    def by_name(cls, name: str)-> Dict[bool, List[Clients]]:
        """Find by name """
        
        raise Exception("Should implement method: by_name")
    
    @abstractclassmethod
    def by_user_id(cls, user_id: str)-> Dict[bool, List[Clients]]:
        """Find by user id """
        
        raise Exception("Should implement method: by_name")