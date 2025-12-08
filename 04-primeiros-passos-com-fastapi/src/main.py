from datetime import UTC, datetime

from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {"title": f"Criando uma aplicação com Django", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app FastAPI", "date": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com Plone", "date": datetime.now(UTC), "published": False},
    {"title": f"Internacionalizando uma app Flask", "date": datetime.now(UTC), "published": True}
]


@app.get("/posts")
def read_posts( published: bool = True, skip: int = 0, limit: int = len(fake_db)):
    return [post for post in fake_db[skip: skip + limit] if post["published"] is published]


@app.get('/post/{framework}')
def read_framework_posts(framework: str):
    return {"posts": [
        {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
        {"title": f"Internacionalizando uma app {framework}", "date": datetime.now(UTC)}
    ]}
