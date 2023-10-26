from pydantic import BaseModel


class PresentmentPrice(BaseModel):
    currency_code: str
    amount: str  # Se mantiene como cadena para evitar problemas de precisión con los números flotantes

