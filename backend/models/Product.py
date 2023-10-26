from typing import List, Optional
from pydantic import BaseModel, validator
from datetime import datetime
from .ProductOption import ProductOption
from .ProductVariant import ProductVariant
from .Image import Image


class Product(BaseModel):
    body_html: str
    created_at: datetime
    handle: str
    id: int
    images: List[Image]
    options: List[ProductOption]
    product_type: str
    published_at: datetime
    published_scope: str
    status: str
    tags: str
    template_suffix: Optional[str]  # Este campo podría no existir, o ser null
    title: str
    updated_at: datetime
    variants: List[ProductVariant]
    vendor: str

    def get_variant_price(self, variant_index=0, currency_code="USD"):
        if variant_index < len(self.variants):
            return self.variants[variant_index].get_price(currency_code)
        return None