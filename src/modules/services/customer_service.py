from dataclasses import dataclass

from src.modules.datalayer.interfaces.customer_repository_interface import (
    CustomerRepositoryInterface,
)
from src.modules.domains.customer import Customer, CustomerRegister
from src.modules.services.base import ServiceBase
from src.modules.services.exception.customer_exception import (
    EmailAlreadyExists,
)


@dataclass
class CustomerService(ServiceBase):
    repository: CustomerRepositoryInterface

    async def register(
        self, customer_registration: CustomerRegister
    ) -> Customer:
        if await self.email_already_exists(customer_registration.email):
            raise EmailAlreadyExists()
        return await self.repository.register(customer_registration)

    async def email_already_exists(self, email: str) -> bool:
        return await self.repository.email_already_exists(email)
