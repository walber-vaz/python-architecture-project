from datetime import datetime
from uuid import UUID

import pytest

from src.modules.domains.customer import CustomerAddress, CustomerRegister
from src.modules.factories.customer_factory import CustomerFactory
from src.modules.services.exception.customer_exception import (
    EmailAlreadyExists,
)


@pytest.mark.asyncio
async def test_should_create_customer():
    service = CustomerFactory.create_mock()

    address = CustomerAddress(
        street="Rua dos Bobos",
        city="São Paulo",
        complement="",
        country="Brasil",
        number="0",
        zipcode="00000-000",
        state="SP",
    )
    customer = CustomerRegister(
        name="John Doe",
        email="jd@email.com",
        password="12345678",
        confirm_password="12345678",
        address=address,
    )

    response = await service.register(customer_registration=customer)

    assert response is not None
    assert response.id is not None
    assert response.name == customer.name
    assert response.email == customer.email
    assert response.address.street == customer.address.street
    assert response.address.city == customer.address.city
    assert response.address.complement == customer.address.complement
    assert response.address.country == customer.address.country
    assert response.address.number == customer.address.number
    assert response.address.zipcode == customer.address.zipcode
    assert response.address.state == customer.address.state

    assert isinstance(response.id, UUID)
    assert isinstance(response.created_at, datetime)
    assert isinstance(response.updated_at, datetime)


@pytest.mark.asyncio
async def test_should_return_error_email_already_exists():
    service = CustomerFactory.create_mock()

    address = CustomerAddress(
        street="Rua dos Bobos",
        city="São Paulo",
        complement="",
        country="Brasil",
        number="0",
        zipcode="00000-000",
        state="SP",
    )
    customer = CustomerRegister(
        name="John Doe",
        email="jd@email.com",
        password="12345678",
        confirm_password="12345678",
        address=address,
    )

    with pytest.raises(EmailAlreadyExists) as excinfo:
        await service.register(customer_registration=customer)

    assert excinfo.type == EmailAlreadyExists
    assert str(excinfo.value) == "Email already exists"
