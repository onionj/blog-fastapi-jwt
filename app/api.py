from fastapi import FastAPI


app = FastAPI(title="blog")

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to your blog!."}