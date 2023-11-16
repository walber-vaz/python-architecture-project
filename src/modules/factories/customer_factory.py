from src.modules.datalayer.repositories.mock.customer_repository_mock import (
    CustomerRepositoryMock,
)
from src.modules.services.customer_service import CustomerService


class CustomerFactory:
    @staticmethod
    def create_mock():
        repository = CustomerRepositoryMock()
        service = CustomerService(repository=repository)
        return service
