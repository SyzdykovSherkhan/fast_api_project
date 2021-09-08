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
    hashed_password = auth_service.hash_password(password=user.password)

    new_user_params = user.copy(update={'password': hashed_password})
    new_user_updated = UserInDB(**new_user_params.dict())

    db_user = User(**new_user_updated.dict())
    async with LocalAsyncSession() as session:
        async with session.begin():
            session.add(db_user)
            await session.flush()
    return db_user
