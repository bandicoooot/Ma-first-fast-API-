from typing import Dict, List 
from fastapi import HTTPException
from src.schemas import Product, ProductCreate, ProductUpdate,producktBase

#kurtzfristige Datenbank
products_db:Dict[int, Product] = {}
next_id: int=1 # Auto id



def create_product(product_data:ProductCreate) -> Product:
    global next_id
    new_product = Product(id=next_id, **product_data.dict())
    products_db [next_id] = new_product
    next_id +=1
    return new_product



def get_product(product_id: int) -> Product:
    if product_id not in products_db:
        raise HTTPException (status_code = 404, detail="Product not found")#
    return products_db[product_id]


def get_all_product() -> List[Product]:
    return list(products_db.values())


def update_product(product_id :int, product_data: ProductUpdate) ->Product:
    if product_id not in products_db:
        raise HTTPException(status_code = 404, detail= "product not found")
    
    existing_product = products_db[product_id]
    update_product = existing_product.copy(update= product_data.dict(exclude_unset= True))
    products_db[product_id] = update_product
    return update_product



def delete_product(product_id: int) ->None:
    if product_id not in product_id:
        raise HTTPException(status_code = 404, detail=("Product not found"))
    del products_db[product_id]