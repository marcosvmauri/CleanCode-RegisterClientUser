from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users

class UserRepositoryInterface(ABC):
    """Interface to User Repository"""
    
    @abstractmethod
    def insert(self, name: str, password: str)-> Users:
        """insert user"""
        
        raise Exception("Method not implemented")
    
    @abstractmethod
    def select(self, user_id: int = None, name: str = None)-> List[Users]:
        """select user"""
        
        raise Exception("Method not implemented")