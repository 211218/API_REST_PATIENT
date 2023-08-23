from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User
from fastapi.responses import JSONResponse

user = APIRouter()

@user.get('/users/list', tags=["users"], response_model=list[User], description="Get all users")
def get_all_users():
    users_rows = conn.execute(users.select()).fetchall()
    users_dicts = [row._asdict() for row in users_rows]
    return JSONResponse(content=users_dicts)

@user.post('/create_user', tags=["users"], response_model=User)
def create_user(user: User):
    try:
        new_user = {"username": user.username, "email": user.email, "password": user.password}
        result = conn.execute(users.insert().values(new_user))
        conn.commit()  # Commit the changes
        created_user_id = result.lastrowid
        created_user = {**new_user, "id": created_user_id}
        return created_user
    except Exception as e:
        print("Error:", e)
        raise


@user.delete('/users/delete/{email}', tags=["users"], description="Delete user by email")
def delete_user(email: str):
    try:
        conn.execute(users.delete().where(users.c.email == email))
        conn.commit()
        return {"message": "User deleted"}
    except Exception as e:
        print("Error:", e)
        raise


@user.put('/users/update/{email}', tags=["users"], response_model=User, description="Update user by email")
def update_user(email: str, user: User):
    try:
        conn.execute(
            users.update().values(username=user.username, email=user.email, password=user.password).where(
                users.c.email == email
            )
        )
        conn.commit()
        return user
    except Exception as e:
        print("Error:", e)
        raise