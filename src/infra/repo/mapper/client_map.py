from enum import unique
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.domain.models.users import Users
from src.infra.config import Base

class ClientMap(Base):
    """Client Map"""
    
    __tablename__ = "Clients"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    user_id = Column(Integer)
    
    def __repr__(self):
        return f"Client: [name={self.name}, user_id={self.user_id}]"
    
    def __eq__(self, other):
        if(
            self.id == other.id
            and self.name == other.name
            and self.user_id == other.user_id
        ):
            return True
        return False