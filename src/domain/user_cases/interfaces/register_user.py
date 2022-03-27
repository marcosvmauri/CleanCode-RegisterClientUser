from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import Users

class RegisterUser(ABC):
    """Interface User Case to Register User"""

    @abstractclassmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        raise Exception("Should implement method: register")