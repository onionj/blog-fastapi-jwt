from typing import List

from fastapi import FastAPI, Path, Body, status, HTTPException, Depends

from app.model import PostOut, PostIn, UserIn
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer

# fake database
posts = [
    {
        "id": 1,
        "title": "test post",
        "content": "Lorem Ipsum ..."
    }
]

users = []


def check_user(data: UserIn):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


app = FastAPI(title="blog")


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to your blog!."}


@app.get("/posts", tags=["posts"], response_model=List[PostOut])
async def get_posts():
    return posts


@app.get("/posts/{id}", tags=["posts"], response_model=PostOut)
async def get_single_post(id: int = Path(..., ge=1)):

    # i use fake database for this sample
    for post in posts:
        if post["id"] == id:
            return post

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        headers={"error": "No such post with the supplied ID."}
    )


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"], response_model=PostOut)
async def add_post(post: PostIn):
    post = post.dict()
    post["id"] = len(posts) + 1
    posts.append(post)
    return post


@app.post("/user/signup", tags=["user"])
async def create_user(user: UserIn = Body(...)):
    # replace with db call, making sure to hash the password first
    users.append(user)
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
async def user_login(user: UserIn = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
