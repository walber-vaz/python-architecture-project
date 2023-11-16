from src.modules.datalayer.interfaces.customer_repository_interface import (
    CustomerRepositoryInterface,
)
from src.modules.datalayer.repositories.mock.memdb import CUSTOMER_DB
from src.modules.domains.customer import Customer, CustomerRegister


class CustomerRepositoryMock(CustomerRepositoryInterface):
    async def register(
        self, customer_registration: CustomerRegister
    ) -> Customer:
        customer: Customer = Customer(**customer_registration.model_dump())
        CUSTOMER_DB.append(customer)
        return customer

    async def email_already_exists(self, email: str) -> bool:
        email_exists = list(
            filter(lambda customer: customer.email == email, CUSTOMER_DB)
        )
        return True if len(email_exists) > 0 else False
