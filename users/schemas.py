from typing import Optional
from pydantic import BaseModel, EmailStr, constr

from fast_api_project import schemas


class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orm_mode = True


class UserCreate(schemas.CreatedModifiedMixin, UserBase):
    email: EmailStr
    password: constr(min_length=8, max_length=50)

    class Config:
        orm_mode = True


class UserInDB(schemas.CreatedModifiedMixin, UserBase):
    password: str

    class Config:
        orm_mode = True


class UserPublic(UserBase):
    class Config:
        orm_mode = True
