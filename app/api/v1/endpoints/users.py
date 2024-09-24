from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()

@router.get("/login")
def login(user: dict = Depends(get_current_user)):
    """
    This route tests Basic Authentication by checking the user's credentials
    and returning a success message based on the user type.
    """
    return {"message": f"Hello {user['email']}, you are logged in as {user['user_type']}"}
