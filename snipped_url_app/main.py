import secrets
import validators
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import schemas, models

from .connectdb import engine, SessionLocal, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


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
def shorten_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Ooopsies :(, Your provided URL is not valid")
        return f"TODO: Create database entry for: {url.target_url}"

    else:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "".join(secrets.choice(chars) for _ in range(5))
        secret_key = "".join(secrets.choice(chars) for _ in range(8))
        db_url = models.URL(
            target_url=url.target_url, key=key, secret_key=secret_key
        )
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        db_url.url = key
        db_url.admin_url = secret_key

        return db_url
