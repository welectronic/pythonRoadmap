from typing import List, Optional
from pydantic import BaseModel, validator
from datetime import datetime
from .VariantOption import VariantOption
from .PresentmentPrice import PresentmentPrice

class ProductVariant(BaseModel):
    barcode: Optional[str]
    compare_at_price: Optional[str]
    created_at: datetime
    fulfillment_service: str
    grams: int
    id: int
    image_id: Optional[int]
    inventory_item_id: int
    inventory_management: str
    inventory_policy: str
    inventory_quantity: int
    old_inventory_quantity: int
    option: VariantOption
    price: List[PresentmentPrice]
    position: int
    product_id: int
    requires_shipping: bool
    sku: Optional[str]
    taxable: bool
    title: str
    updated_at: datetime
    weight: float
    weight_unit: str

    # Aquí podríamos añadir validadores si necesitamos comprobaciones específicas de los campos
    # # Por ejemplo, un validador simple para asegurar que el 'price' en las variantes no sea negativo
    @validator('price', each_item=True)
    def validate_price(cls, p):
        if float(p.amount) < 0:
            raise ValueError("El precio no puede ser negativo")

    # Devuelve el precio sin modificaciones
    def get_price(self, currency_code="USD"): 
        # Aquí buscamos el precio según el código de moneda proporcionado
        for p in self.price:
            if p.currency_code == currency_code:
                return float(p.amount)
        return None
