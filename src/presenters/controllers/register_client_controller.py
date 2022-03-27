from typing import Type
from src.main.interface import RouteInterface
from src.domain.user_cases.interfaces import RegisterClient
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErros


class RegisterClientController(RouteInterface):
    """ Class to Define Route to register_client use case """

    def __init__(self, register_client_use_case: Type[RegisterClient]):
        self.register_client_use_case = register_client_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        if http_request.body:
            
            body_params = http_request.body.keys()

            if ("name" in body_params and "user_id" in body_params):
                
                name = http_request.body["name"]
                user_id = http_request.body["user_id"]
                
                response = self.register_client_use_case.register(
                        name=name,
                        user_id=user_id,
                    )
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErros.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        https_error = HttpErros.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )