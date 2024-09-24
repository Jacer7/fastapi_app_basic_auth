from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import json
import secrets

security = HTTPBasic()

# Load users from JSON (mocking a database)
with open('app/data/users.json', 'r') as f:
    users_db = json.load(f)

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    # Find user in JSON database
    user = users_db.get(credentials.username)
    
    # Validate user existence and password (using constant time comparison for security)
    if user and secrets.compare_digest(user['password'], credentials.password):
        return user

    # Raise exception if the user is invalid
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Basic"},
    )

def get_admin_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = users_db.get(credentials.username)
    if user["user_type"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    elif user and secrets.compare_digest(user['password'], credentials.password):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
    )
