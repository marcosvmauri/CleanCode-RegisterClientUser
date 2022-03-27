from typing import Dict, List
from src.domain.models import Users, Clients
from src.domain.test import mock_client, mock_user


class RegisterClientSpy:
    """ Class to define usecase: Register Client """

    def __init__(self, client_repository: any, find_user: any):
        self.client_repository = client_repository
        self.registry_param = {}

    def registry(
        self, name: str, user_id: int) -> Dict[bool, Clients]:
        """ Registry client """

        self.registry_param["name"] = name
        self.registry_param["user_id"] = user_id
        
        response = None

        validate_client = isinstance(name, str) and isinstance(user_id, int)
       
        if validate_client:
            response = mock_client()

        return {"Success": validate_client, "Data": response}
