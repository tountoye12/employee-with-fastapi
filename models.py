from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax : float | None = None


    def __str__(self) -> str:
        return self.name