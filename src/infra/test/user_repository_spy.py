from typing import List
from src.domain.models.users import Users
from src.domain.test import mock_user


class UserRepositorySpy:
    """Spy to User Repository"""
    
    def __init__(self):
        self.insert_user_parmas = {}
        self.select_user_parmas = {}
        
    def insert(self, name:str, password: str) -> Users:
        """Spy to all the atributes"""
        
        self.insert_user_parmas["name"] = name
        self.insert_user_parmas["password"] = password
        
        return mock_user()
    
    def select(self, user_id = None, name = None) -> List[Users]:
        """Spy to all the atributes"""
        
        self.select_user_parmas["user_id"] = user_id
        self.select_user_parmas["name"] = name
        
        return mock_user()