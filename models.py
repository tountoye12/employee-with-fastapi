from pydantic import BaseModel


class Image(BaseModel):
   url: str
   name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax : float | None = None

    image: Image | None = None


    def __str__(self) -> str:
      return self.name


