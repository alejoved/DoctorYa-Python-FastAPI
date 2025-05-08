from pydantic import BaseModel


class LoginDTO(BaseModel):
    identification: str
    password: str
    