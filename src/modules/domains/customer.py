from typing import Optional

from pydantic import BaseModel, EmailStr

from src.modules.domains.base import DomainBase


class CustomerAddress(BaseModel):
    street: str
    number: Optional[str]
    complement: Optional[str]
    city: str
    state: str
    country: str
    zipcode: str


class Customer(DomainBase):
    name: str
    email: EmailStr
    address: CustomerAddress


class CustomerRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str
    address: CustomerAddress
