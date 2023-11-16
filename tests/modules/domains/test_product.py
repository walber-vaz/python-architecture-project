from src.modules.domains.product import Product


def test_should_create_product():
    product = Product(
        name="Notebook",
        description="Notebook Dell",
        price=3500,
    )

    assert product.name == "Notebook"
    assert product.description == "Notebook Dell"
    assert product.price == 3500
