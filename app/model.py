from pydantic import BaseModel, Field, EmailStr


class PostBase(BaseModel):
    title: str = Field(..., exaample="FastAPI")
    content: str = Field(...,
                         example="Securing FastAPI applications with JWT.")


class PostOut(PostBase):
    id: int


class PostIn(PostBase):
    pass
