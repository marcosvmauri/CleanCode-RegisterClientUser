from typing import Type
from src.main.interface import RouteInterface
from src.domain.user_cases.interfaces import FindUser
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.erros import HttpErros


class FindUserController(RouteInterface):
    """Class to define controller to find_user use case"""
    
    def __init__(self,find_user:Type[FindUser]):
        self.find_user = find_user
        
    def route(self,http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""
        
        response = None
        
        if http_request.query:
            query_string_params = http_request.query.keys()
            if "user_id" in query_string_params and "user_name" not in query_string_params:
                user_id = http_request.query["user_id"]
                response = self.find_user.by_id(user_id)
            elif ("user_name" in query_string_params and "user_id" not in query_string_params):
                user_name = http_request.query["user_name"]
                response = self.find_user.by_name(user_name)
            else:
                response = {"Success": False, "Data": None}
                
            if response["Success"] is False:
                http_error = HttpErros.error_422();
                return HttpResponse(status_code = http_error, body= http_error["body"])
            
            if response["Data"] == []:
                https_error = HttpErros.error_401()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )
            
            return HttpResponse(status_code = 200, body=response["Data"])
        
        http_error = HttpErros.error_400()
        return HttpResponse(status_code = http_error, body= http_error["body"])
    