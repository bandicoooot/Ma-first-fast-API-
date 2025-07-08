from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class producktBase(BaseModel):
    name: str = Field(..., example="Wireless headphones")
    price: float =Field(..., example = 99.99)
    category : str = Field(..., examples= "Electronics")
    stock: int = Field(..., example = 50)


class ProductCreate(producktBase):
    pass




class Product(producktBase):
    id: int 


class ProductUpdate(producktBase):
    pass