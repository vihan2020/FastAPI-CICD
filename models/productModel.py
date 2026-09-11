from typing import Optional

from pydantic import BaseModel, Field

# Product model
class Product(BaseModel):
    id: Optional[str] = None
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(ge=0)
    description: str = Field(default="", max_length=1000)
