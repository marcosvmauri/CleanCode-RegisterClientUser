from typing import Type
from src.main.interface import RouteInterface
from src.domain.user_cases.interfaces import FindClient
from src.presenters.helpers import HttpResponse, HttpRequest
from src.presenters.erros import HttpErros


class FindClientController(RouteInterface):
    """ Class to define Route to find_client use case """

    def __init__(self, find_client_use_case: Type[FindClient]):
        self.find_client_use_case = find_client_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpRequest:
        """ Method to call use case """

        response = None

        if http_request.query:
            
            query_string_params = http_request.query.keys()

            if "client_id" in query_string_params and "user_id"not in query_string_params and "name" not in query_string_params:
                client_id = http_request.query["client_id"]
                response = self.find_client_use_case.by_id(client_id=client_id)
            elif (
                "user_id" in query_string_params and "client_id" not in query_string_params and "name" not in query_string_params
            ):
                user_id = http_request.query["user_id"]
                response = self.find_client_use_case.by_user_id(user_id=user_id)
            elif (
                "user_id" not in query_string_params and "client_id" not in query_string_params and "name" in query_string_params
            ):
                name = http_request.query["name"]
                response = self.find_client_use_case.by_name(name=name)
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErros.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )
            
            if response["Data"] == []:
                https_error = HttpErros.error_401()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )
            
            return HttpResponse(status_code=200, body=response["Data"])

        https_error = HttpErros.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
        