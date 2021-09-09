from typing import List

from fastapi import FastAPI, HTTPException, Path, status

from app.model import PostOut, PostIn

# fake database
posts = [
    {
        "id": 1,
        "title": "test post",
        "content": "Lorem Ipsum ..."
    }
]

users = []

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


@app.post("/posts", tags=["posts"], response_model=PostOut)
async def add_post(post: PostIn):
    post = post.dict()
    post["id"] = len(posts) + 1
    posts.append(post)

    return post
