from datetime import UTC, datetime
from pydantic import BaseModel

from fastapi import FastAPI, status

app = FastAPI()

fake_db = [
    {"title": f"Criando uma aplicação com Django", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app FastAPI", "date": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com Plone", "date": datetime.now(UTC), "published": False},
    {"title": f"Internacionalizando uma app Flask", "date": datetime.now(UTC), "published": True}
]

class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False
    author: str


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    fake_db.append(post.model_dump())
    return post


@app.get("/posts")
def read_posts( published: bool, limit: int, skip: int = 0):
# def read_posts( published: bool = True, skip: int = 0, limit: int = len(fake_db)):
    return [post for post in fake_db[skip: skip + limit] if post["published"] is published]
    # posts = []
    # for post in fake_db:
    #     if len(posts) == limit:
    #         break
    #     if post["published"] is published:
    #         posts.append(post)
    
    # return posts
        


@app.get('/post/{framework}')
def read_framework_posts(framework: str):
    return {"posts": [
        {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
        {"title": f"Internacionalizando uma app {framework}", "date": datetime.now(UTC)}
    ]}
