from fastapi import APIRouter, status, Body
from fastapi.responses import Response

from users import auth_service
from users.schemas import UserCreate, UserInDB, UserPublic
from users.models import User
from fast_api_project import LocalAsyncSession

router = APIRouter()


@router.post('/create', tags=['user registration'],
             description='Register the User', response_model=UserPublic)
async def user_create(user: UserCreate):
    hashed_password = auth_service.hash_password(user.password)
    db_user = User(email=user.email, password=hashed_password)
    async with LocalAsyncSession() as session:
        async with session.begin():
            await session.add(db_user)
            await session.commit()
            await session.refresh(db_user)
    return db_user
