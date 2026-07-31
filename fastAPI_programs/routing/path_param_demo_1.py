from fastapi import FastAPI
from data.product_data import products

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Product API"}


@app.get("/products")
def get_products():
    return products


@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "error":"No Product Found"
    }