from typing import List
from pydantic import BaseModel

class ProductOption(BaseModel):
    id: int
    product_id: int
    name: str
    position: int
    values: List[str]  # Lista de valores como colores, tamaños, etc