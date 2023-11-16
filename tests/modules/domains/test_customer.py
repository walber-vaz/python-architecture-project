from src.modules.domains.customer import Customer, CustomerAddress


def test_should_create_customer():
    address = CustomerAddress(
        street="Rua dos Bobos",
        number="0",
        complement="",
        city="São Paulo",
        state="SP",
        country="Brasil",
        zipcode="00000-000",
    )
    customer = Customer(
        name="John Doe", email="jhon_doe@email.com", address=address
    )

    assert customer.name == "John Doe"
    assert customer.email == "jhon_doe@email.com"
    assert customer.address.street == "Rua dos Bobos"
    assert customer.address.number == "0"
    assert customer.address.complement == ""
    assert customer.address.city == "São Paulo"
    assert customer.address.state == "SP"
    assert customer.address.country == "Brasil"
    assert customer.address.zipcode == "00000-000"
