from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_blog():
    return "blog app created!"
