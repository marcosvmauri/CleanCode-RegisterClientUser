from typing import Type, Dict
from src.domain.user_cases.interfaces import RegisterUser as RegisterUserInterface
from src.domain.models import Users
from src.infra.repo.interfaces.user_repository_interface import UserRepositoryInterface

class RegisterUser(RegisterUserInterface):
    """Class to define usercase Register User"""
    
    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository
        
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user case
        :param  - name: The name of the user
                - password: The password of the user
        :return - Dictionary with information of the process"""
        
        response = None
        validate_user = isinstance(name,str) and isinstance(password,str)
        
        if validate_user:
            response = self.user_repository.insert(name, password)
            
        return {"Success": validate_user, "Data": response}
        