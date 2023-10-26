import re
from typing import List
from pydantic import BaseModel, HttpUrl, validator
from datetime import datetime
class Image(BaseModel):
    id: int
    product_id: int
    position: int
    created_at: datetime
    updated_at: datetime
    width: int
    height: int
    src: HttpUrl  # Aseguramos que la URL de la imagen sea válida
    variant_ids: List[int]  # Asumiendo que los ids de las variantes son enteros
@validator('src')
def check_url(cls, v):
    # debe tener la estructura de una URL válida con expresiones regulares
    regex = r'^https?:\/\/[A-Za-z0-9]+\.[A-Za-z0-9]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$'
    if not re.match(regex, str(v)):
        raise ValueError("La URL no es válida")
    return v
