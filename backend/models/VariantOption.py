from pydantic import BaseModel
class VariantOption(BaseModel):
    option1: str  # Si hay más opciones, puedes añadir 'option2', 'option3', etc.
    option2: str
    # option3 es opcional
    option3: str = None

