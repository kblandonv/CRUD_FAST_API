from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Create a User model
# Create a class for the user


class User(BaseModel):
    username: str
    password: str
    name: str
    lastname: str
    address: str
    telephone: Optional[int]
    email: str
    creation_user: datetime = datetime.now()

# Create a UpdateUser model
# Create a class for the UpdateUser

class UpdateUser(BaseModel):
    username: str = None
    password: str = None
    name: str = None
    lastname: str = None
    address: str = None
    telephone: int = None
    email: str = None

# Create UserId model
# Create a class for the UserId
class UserId(BaseModel):
    id: int

# Create a ShowUser model
# Create a class for the ShowUser
class ShowUser(BaseModel):
    username: str
    name: str
    lastname: str
    email: str
    class Config():
        orm_mode = True