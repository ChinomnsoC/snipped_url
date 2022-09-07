import secrets
import validators
from fastapi import Depends, FastAPI, HTTPException
from snipped_url_db import models, schemas

from ..snipped_url_db.database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return "Welcome to the snipped_url App"


@app.post("/url", response_model=schemas.URLInfo)
def shorten_url(url: schemas.URLBase):
    if validators.url(url.target_url):
        pass
    else:
        raise_bad_request(message="Ooopsies :(, Your provided URL is not valid")
    return f"TODO: Create database entry for: {url.target_url}"
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
