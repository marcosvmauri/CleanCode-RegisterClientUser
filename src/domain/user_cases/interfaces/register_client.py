from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import Clients

class RegisterClient(ABC):
    """Interface Client Case to Register User"""

    @abstractclassmethod
    def register(cls, name: str, user_information: Dict[int, str] ) -> Dict[bool, Clients]:
        raise Exception("Should implement method: register")