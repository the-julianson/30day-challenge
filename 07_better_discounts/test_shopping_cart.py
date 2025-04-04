import pytest  # type: ignore
from solution import Item
from decimal import Decimal

@pytest.fixture
def sample_item(name: str="Apple", price: Decimal=Decimal("2.0"), quantity: int=3) -> Item:
    return Item(name=name, price=price, quantity=quantity)

def test_item_creation(sample_item: Item) -> None:
    assert sample_item.name == "Apple"
    assert sample_item.price == Decimal("2.0")
    assert sample_item.quantity == 3

def test_item_subtotal_calculation(sample_item: Item) -> None:
    assert sample_item.subtotal == Decimal("6.0")
    