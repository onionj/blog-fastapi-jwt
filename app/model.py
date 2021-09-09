from pydantic import BaseModel, Field, EmailStr


class PostBase(BaseModel):
    title: str = Field(..., exaample="FastAPI")
    content: str = Field(...,
                         example="Securing FastAPI applications with JWT.")


class PostOut(PostBase):
    id: int = Field(..., example=1)


class PostIn(PostBase):
    pass


class UserBase(BaseModel):
    email: EmailStr = Field(..., example="example@gmail.com")


class UserIn(UserBase):
    password: str = Field(..., min_length=8)
