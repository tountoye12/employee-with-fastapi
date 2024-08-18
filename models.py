from pydantic import BaseModel, HttpUrl, EmailStr


class Image(BaseModel):
   url: HttpUrl
   name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax : float | None = None

    image: Image | None = None


    def __str__(self) -> str:
      return self.name



class BaseUser(BaseModel):
   username: str
   email: EmailStr
   full_name: str | None = None


class UserIn(BaseUser):
   password: str