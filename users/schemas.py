from typing import Optional
from pydantic import BaseModel, EmailStr, constr

from fast_api_project import schemas


class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: constr(min_length=8, max_length=50)


class UserInDB(schemas.IdModelMixin, schemas.CreatedModifiedMixin, UserBase):
    password: constr(min_length=8, max_lenght=50)


class UserPublic(schemas.IdModelMixin, UserBase):
    ...
