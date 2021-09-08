from fast_api_project import LocalAsyncSession

from users import auth_service
from users.models import User
from users.schemas import UserCreate, UserInDB


async def user_create(user: UserCreate) -> UserInDB:
    hashed_password = auth_service.hash_password(password=user.password)
    db_user = User(email=user.email, password=hashed_password)
    async with LocalAsyncSession() as session:
        async with session.begin():
            session.add(db_user)
            await session.flush()