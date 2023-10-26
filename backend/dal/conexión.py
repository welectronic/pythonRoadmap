import json
from typing import List
from backend.models.Product import Product  


def load_products_from_json(filepath: str) -> List[dict]:
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def create_product_objects(product_data: List[dict]) -> List[Product]:
    products = []
    for item in product_data:
        product = Product(**item)
        products.append(product)
    return products
