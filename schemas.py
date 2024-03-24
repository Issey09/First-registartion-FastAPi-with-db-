from fastapi import Form
from pydantic import BaseModel


class UserS(BaseModel):
    password: str
class User(UserS):
    login:  str
