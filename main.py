from fastapi import FastAPI

app = FastAPI()

products = {
    1: {"item": "milk", "price": 3, "amount": 5},
    2: {"item": "bread", "price": 2, "amount": 5},
    3: {"item": "eggs", "price": 3, "amount": 5},
    4: {"item": "apples", "price": 1, "amount": 5},
    5: {"item": "rice", "price": 1, "amount": 5},
}

@app.get("/")
def home():
    return {"products": len(products)}

@app.get("/products/{id_products}")
def view_product(id_products: int):
    if id_products in products:
        return products[id_products]
    else:
        return{"Error": "ID Product Invalid"}





