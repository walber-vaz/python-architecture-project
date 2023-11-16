from src.modules.domains.base import DomainBase


class Product(DomainBase):
    name: str
    description: str
    price: float
