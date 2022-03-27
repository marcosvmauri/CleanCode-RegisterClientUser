from typing import Type, Dict, List
from src.domain.models import Users
from src.domain.test import mock_user

class FindUserSpy():
    """Class to define usercase Register User"""
    
    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.by_id_param = {}
        self.by_name_param = {}
        self.by_id_and_name_param = {}

        
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select user by id
        :param  - user_id: id of the user
        :return - Dictionary with information of the process"""
        
        self.by_id_param["user_id"] = user_id
        response = None
        validate_user = isinstance(user_id, int)

        if validate_user:
            response = [mock_user()]

        return {"Success": validate_user, "Data": response}
    
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select User By name
        :param - name: name of the user
        :param - Dictionary with informations of the process
        """

        self.by_name_param["name"] = name
        response = None
        validate_user = isinstance(name, str)

        if validate_user:
            response = [mock_user()]
            
        return {"Success": validate_user, "Data": response}
        