import validators
from fastapi import FastAPI, HTTPException
from snipped_url.snipped_url_db import schemas

app = FastAPI()


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


@app.get("/")
def read_root():
    return "Welcome to the snipped_url App"


@app.post("/url")
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
