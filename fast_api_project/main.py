import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.append('..')  # fixing parent folder import error

from fast_api_project import settings
from users.api.controller import router as user_router


def get_application():
    _app = FastAPI()

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in
                       settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(user_router, prefix='/users')  # this is the new added

    return _app


app = get_application()