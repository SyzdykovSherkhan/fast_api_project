from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from fast_api_project import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String(50), nullable=False)

    first_name = Column(String(100))
    last_name = Column(String(100))

