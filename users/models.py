from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from fast_api_project import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(50), nullable=False)

    is_active = Column(Boolean, nullable=False, server_default='True')
    is_superuser = Column(Boolean, nullable=False, server_default='False')
    is_verified = Column(Boolean, nullable=False, server_default='False')

    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)

    first_name = Column(String(100))
    last_name = Column(String(100))

