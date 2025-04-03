from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from copy import deepcopy


PRICE_ERROR_MSG = "Price cannot be negative"
QUANTITY_ERROR_MSG = "Quantity cannot be negative"

class ItemNotFoundException(Exception):
    pass

@dataclass
class Item:
    _name: str
    _price: Decimal
    _quantity: int

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> Decimal:
        return self._price
    
    @price.setter
    def price(self, value: Decimal) -> None:
        if value < Decimal("0"):
            raise ValueError(PRICE_ERROR_MSG)
        self._price = value

    
    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int ) -> None:
        if value < 0:
            raise ValueError(QUANTITY_ERROR_MSG)
        self._quantity = value

    @property
    def sub_total(self) -> Decimal:
        return self.quantity * self.price

    def __post_init__(self) -> None:
        if self._price < Decimal("0"):
            raise ValueError(PRICE_ERROR_MSG)
        if self._quantity < 0:
            raise ValueError(QUANTITY_ERROR_MSG)

    


@dataclass
class ShoppingCart:
    _items: list[Item] = field(default_factory=list)
    _discount_code: Optional[str] = None

    @property
    def items(self) -> list[Item]:
        return deepcopy(self._items)
    
    @items.setter
    def items(self, value: list[Item]) -> None:
        self._items = deepcopy(value)

    @property
    def discount_code(self) -> Optional[str]:
        return self._discount_code
    
    @discount_code.setter
    def discount_code(self, value: Optional[str]) -> None:
        self._discount_code = value

    def add_item(self, item: Item) -> None:
        """Adds an item to the cart using deep copy."""
        self._items.append(deepcopy(item))

    def find_item_index(self, item_name: str) -> int:
        """Finds the index of an item by name."""
        for index, item in enumerate(self._items):
            if item.name == item_name:
                return index
        raise ItemNotFoundException(f"Item '{item_name}' not found.")

    def remove_item(self, item_name: str) -> None:
        """Removes an item by name using index-based removal."""
        index = self.find_item_index(item_name)
        self._items.pop(index)

    def find_item(self, item_name: str) -> Item:
        found_item_index = self.find_item_index(item_name)
        return self._items[found_item_index]

    def update_item_quantity(self, item_name: str, updated_quantity: int) -> None:
        found_item = self.find_item(item_name)
        found_item.quantity = updated_quantity

    def update_item_price(self, item_name: str, new_price: Decimal) -> None:
        found_item= self.find_item(item_name)
        found_item.price = new_price

    @property
    def total(self) -> Decimal:
        return Decimal(sum(item.sub_total for item in self.items))
    
    def display(self) -> None:
        # Print the cart
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.sub_total:>7.2f}"
            )
        print("=" * 40)
        print(f"Total:    ${self.total:>7.2f}")

    

def main() -> None:
    # Create a shopping cart and add some items to it
    my_items = [
        Item("Apple", Decimal("1.5"), 10),
        Item("Banana", Decimal("2"), 2),
        Item("Pizza", Decimal("11.90"), 5),
    ]

    cart = ShoppingCart()
    cart.items = my_items

    # Update some items' quantity and price
    cart.update_item_quantity(item_name="Apple", updated_quantity = 10)
    cart.update_item_price(item_name="Pizza", new_price=Decimal("3.50"))

    # Remove an item
    cart.remove_item(item_name="Banana")


    # Print the cart
    cart.display()


if __name__ == "__main__":
    main()

