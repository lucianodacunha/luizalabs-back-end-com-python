from datetime import UTC, datetime
from typing import Annotated

from fastapi import Cookie, Header, Response, status
from schemas.post import PostIn
from views.post import PostOut

from main import app

fake_db = [
    {"title": f"Criando uma aplicação com Django", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app FastAPI", "date": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com Plone", "date": datetime.now(UTC), "published": False},
    {"title": f"Internacionalizando uma app Flask", "date": datetime.now(UTC), "published": True}
]


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post: PostIn):
    fake_db.append(post.model_dump())
    return post


@app.get("/posts", response_model=list[PostOut])
def read_posts(response: Response, published: bool, limit: int, skip: int = 0, 
               ads_id: Annotated[str | None, Cookie()] = None,
               user_agent: Annotated[str | None, Header()] = None):
    response.set_cookie(key="user", value="user@gmail.com")
    print(f"Cookie {ads_id}")
    print(f"User-Agent {user_agent}")
    return [post for post in fake_db[skip: skip + limit] if post["published"] is published]


@app.get('/post/{framework}', response_model=PostOut)
def read_framework_posts(framework: str):
    return {"posts": [
        {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
        {"title": f"Internacionalizando uma app {framework}", "date": datetime.now(UTC)}
    ]}
