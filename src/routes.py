from fastapi import APIRouter, HTTPException
from typing import List,Tuple
from src.schemas import Product, ProductCreate, ProductUpdate
from src.crud import create_product, get_product, get_products, update_product, delete_product

router = APIRouter()

#neue produkte erstellen
@router.post("/products/", response_model=Product, status_code=201)
def create_a_new_product(product: ProductCreate):
    return create_product(product)

#ganze pruduktliste abrufen
@router.get("/products/", response_model = List[Product],status_code=200)
def Retrieeve_all_products():
    return get_products


#einzelnes Produkt abrufen
@router.get("/products/{id}", respone_model = Product, status_code=200)
def Retrive_a_specfic_product(id: int):
    Product = get_product(id)
    if not Product:
        raise HTTPException(status_code = 44, detail="Product not found")
    return Product


#update a product
@router.put("/products/{id}", response_model = Product, status_code= 200)
def update_a_product(id:int, productUpdate: ProductUpdate):
    updated = update_product(id)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


#delette a product
@router.delete("/products/{id}",response_model=Product)
def delete_a_product(id: int):
    deleted = delete_product(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}