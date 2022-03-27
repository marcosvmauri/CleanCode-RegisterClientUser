from typing import Dict, List
from abc import ABC, abstractclassmethod
from src.domain.models import Users

class FindUser(ABC):
    """Interface User Case to Find User"""
    
    @abstractclassmethod
    def by_id(cls, user_id: int)-> Dict[bool, List[Users]]:
        """Find by id """
        
        raise Exception("Should implement method: by_id")
    
    @abstractclassmethod
    def by_name(cls, name: str)-> Dict[bool, List[Users]]:
        """Find by id """
        
        raise Exception("Should implement method: by_name")