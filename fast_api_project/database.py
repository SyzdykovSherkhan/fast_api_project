from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from fast_api_project import settings


DB_URL = f'''postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PORT}
@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'''

async_engine = create_async_engine(DB_URL, echo=True)

LocalAsyncSession = sessionmaker(engine=async_engine, expire_on_commit=False,
                                 class_=AsyncSession)

Base = declarative_base()
