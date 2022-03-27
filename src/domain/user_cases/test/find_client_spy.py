from typing import Dict, List
from src.domain.models import Clients
from src.domain.test import mock_client


class FindClientSpy:
    """ Class to mock usecase: Find Pet """

    def __init__(self, client_repository: any):
        self.client_repository = client_repository
        self.by_client_id_param = {}
        self.by_user_id_param = {}
        self.by_name_param = {}

    def by_id(self, client_id: int) -> Dict[bool, List[Clients]]:
        """ Select Pet By client_id """

        self.by_client_id_param["client_id"] = client_id
        response = None
        validate_entry = isinstance(client_id, int)

        if validate_entry:
            response = [mock_client()]

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Clients]]:
        """ Select Pet By user_id """

        self.by_user_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_client()]

        return {"Success": validate_entry, "Data": response}

    def by_name(self,name:str) -> Dict[bool, Clients]:
        """ Select Pet By user_id """

        self.by_user_id_param["name"] = name
        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_client()]

        return {"Success": validate_entry, "Data": response}