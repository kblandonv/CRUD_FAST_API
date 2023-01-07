from fastapi import APIRouter, Depends
from app.schemas import User, UserId, ShowUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

# Create a new API to get all users

@router.get('/')
def get_users(db: Session = Depends(get_db)):
    data = db.query(models.User).all()
    return data

# Create a new API to create a new user


@router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    username = user.dict()
    # users.append(username)
    new_user = models.User(username=username["username"], password=username["password"], name=username["name"],
                           lastname=username["lastname"], address=username["address"], telephone=username["telephone"], email=username["email"])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return ("User created successfully")

# Create a new API to get a user by id ussing query parameters


@router.get('/{user_id}', response_model=ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return {"Error": "User not found"}
    return user

    # for user in users:
    #    if user["id"] == user_id:
    #        return {"User": user}
    # return {"Error": "User not found"}

# Create a new API to get a user by id ussing path parameters



# Create a new API to update a user by id ussing query parameters


@router.patch("/{user_id}")
def update_user(user_id: int, updateUser: UpdateUser, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        return {"Error": "User not found"}
    user.update(updateUser.dict(exclude_unset=True), synchronize_session=False )
    db.commit()
    return {"User": "User updated successfully"}

    #for index, user in enumerate(users):
    #    if user["id"] == user_id:
    #        users[index]["id"] = updateUser.dict()["id"]
    #        users[index]["username"] = updateUser.dict()["username"]
    #        users[index]["name"] = updateUser.dict()["name"]
    #        users[index]["lastname"] = updateUser.dict()["lastname"]
    #       users[index]["address"] = updateUser.dict()["address"]
    #       users[index]["telephone"] = updateUser.dict()["telephone"]
    #       users[index]["email"] = updateUser.dict()["email"]
    #       return {"User": "User updated successfully"}


# Create a new API to delete a user by id
@router.delete("/{user_id}",)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        return {"Error": "User not found"}
    user.delete(synchronize_session=False)
    db.commit()
    return {"User": "User deleted successfully"}

    """for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"User": "User deleted successfully"}
    return {"Error": "User not found"}
    """
