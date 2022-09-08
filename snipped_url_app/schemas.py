from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str


class URL(URLBase):
    is_active: bool
    clicks: int
    # creator_ip_address: str
    # clicker_ip_address: str

    class Config:
        orm_mode = True


class URLInfo(URL):
    url: str
    admin_url: str
