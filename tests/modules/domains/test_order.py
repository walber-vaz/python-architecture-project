from src.modules.domains.customer import Customer, CustomerAddress
from src.modules.domains.order import (
    Order,
    OrderItem,
    OrderStatus,
    OrderStatusName,
)
from src.modules.domains.product import Product


def test_should_create_order():
    # Pedidor Realizado
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
        name="João da Silva", email="jsilva@gmail.com", address=address
    )
    status1 = OrderStatus()

    product1 = Product(
        name="Notebook", description="Notebook Dell", price=3500
    )
    product2 = Product(name="Mouse", description="Mouse Dell", price=100)

    item1 = OrderItem(product_id=product1.id, price=product1.price, quantity=1)
    item2 = OrderItem(product_id=product2.id, price=product2.price, quantity=1)

    order = Order(customer=customer)
    order.add_item(item1)
    order.add_item(item2)
    order.add_status(status1)

    assert status1.name == OrderStatusName.ACCOMPLISHED

    assert product1.name == "Notebook"
    assert product1.description == "Notebook Dell"
    assert product1.price == 3500

    assert product2.name == "Mouse"
    assert product2.description == "Mouse Dell"
    assert product2.price == 100

    assert len(order.status) == 1
    assert order.customer.name == "João da Silva"
    assert order.customer.email == "jsilva@gmail.com"
    assert order.status[0].name == OrderStatusName.ACCOMPLISHED
    assert len(order.items) == 2

    # Pedidor em preparação
    status2 = OrderStatus(name=OrderStatusName.IN_PREPARATION)
    order.add_status(status2)

    assert len(order.status) == 2
    assert order.status[1].name == OrderStatusName.IN_PREPARATION

    # Pedidor enviado
    status3 = OrderStatus(name=OrderStatusName.SENT)
    order.add_status(status3)

    assert len(order.status) == 3
    assert order.status[2].name == OrderStatusName.SENT
    assert customer.address.street == "Rua dos Bobos"
    assert customer.address.number == "0"
    assert customer.address.complement == ""
    assert customer.address.city == "São Paulo"
    assert customer.address.state == "SP"
    assert customer.address.country == "Brasil"
    assert customer.address.zipcode == "00000-000"

    # Pedidor entregue
    status4 = OrderStatus(name=OrderStatusName.DELIVERED)
    order.add_status(status4)

    assert len(order.status) == 4
    assert order.status[3].name == OrderStatusName.DELIVERED

    # Pedidor finalizado
    status5 = OrderStatus(name=OrderStatusName.FINISHED)
    order.add_status(status5)

    assert len(order.status) == 5
    assert order.status[4].name == OrderStatusName.FINISHED

    assert order.total() == 3600
