from src.modules.datalayer.base import RepositoryInterface
from src.modules.domains.customer import Customer, CustomerRegister


class CustomerRepositoryInterface(RepositoryInterface):
    async def register(
        self, customer_registration: CustomerRegister
    ) -> Customer:
        raise NotImplementedError

    async def email_already_exists(self, email: str) -> bool:
        raise NotImplementedError
