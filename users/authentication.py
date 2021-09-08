from passlib.context import CryptContext

from fast_api_project import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Authenticate:
    @staticmethod
    def hash_password(*, password: str) -> str:
        return pwd_context.hash(password+settings.SECRET_KEY)
