# FastAPI Product API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

A simple FastAPI project to manage a product catalog. This API allows you to view the total number of products and details of a specific product by its ID.

---

## 📋 Code Description

The project consists of a FastAPI application with two endpoints:

1. **`/`**: Returns the total number of available products.
2. **`/products/{id_products}`**: Returns the details of a specific product based on the provided ID.

### Product Structure
Products are stored in a Python dictionary, where each key is an ID and the value is a dictionary containing:
- `item`: Product name.
- `price`: Product price.
- `amount`: Available stock quantity.

Example structure:
```python
products = {
    1: {"item": "milk", "price": 3, "amount": 5},
    2: {"item": "bread", "price": 2, "amount": 5},
    # ...
}
