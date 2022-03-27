from typing import Type, Dict, List
from src.domain.user_cases.interfaces import FindUser as FindUserInterface
from src.domain.models import Users
from src.infra.repo.interfaces.user_repository_interface import UserRepositoryInterface

class FindUser(FindUserInterface):
    """Class to define usercase Register User"""
    
    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository
        
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select user by id
        :param  - user_id: id of the user
        :return - Dictionary with information of the process"""
        
        response = None
        validate_user = isinstance(user_id, int)
        
        if validate_user:
            response = self.user_repository.select(user_id=user_id)
            
        return {"Success": validate_user, "Data": response}
    
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select user by name
        :param  - user_id: id of the user
        :return - Dictionary with information of the process"""
        
        response = None
        validate_user = isinstance(name, str)
        
        if validate_user:
            response = self.user_repository.select(name=name)
            
        return {"Success": validate_user, "Data": response}
        