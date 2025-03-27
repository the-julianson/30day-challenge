from decimal import Decimal
from dataclasses import dataclass
from enum import StrEnum
from typing import Iterable, Protocol, List


class OrderType(StrEnum):
    ONLINE = "online"
    IN_STORE = "in store"


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Order:
    id: int
    type: OrderType
    customer_email: str


@dataclass
class Email:
    body: str
    subject: str
    recipient: str
    sender: str = "sales@webshop.com"  # Default sender


@dataclass
class EmailTemplate:
    subject: str
    body_template: str


def calculate_total_price(items: Iterable[Item]) -> Decimal:
    return Decimal(sum(item.price for item in items))


def calculate_discounted_price(items: Iterable[Item], discount: Decimal) -> Decimal:
    total_price = calculate_total_price(items)  # Reuse existing function
    return total_price - (total_price * discount)


def generate_email(template: EmailTemplate, order: Order) -> Email:
    return Email(
        body=template.body_template.format(order_id=order.id),
        subject=template.subject,
        recipient=order.customer_email,
    )


# Email templates
ORDER_CONFIRMATION = EmailTemplate(
    subject="Order Confirmation",
    body_template="Thank you for your order! Your order #{order_id} has been confirmed."
)

ORDER_SHIPPED = EmailTemplate(
    subject="Order Shipped",
    body_template="Good news! Your order #{order_id} has been shipped and is on its way."
)


class OrderProcessor(Protocol):
    def process(self, order: Order) -> None:
        """Process the order according to its type"""
        pass


class OnlineOrderProcessor:
    def process(self, order: Order) -> None:
        print("Processing online order...")
        print(generate_email(ORDER_CONFIRMATION, order))
        print("Shipping the order...")
        print(generate_email(ORDER_SHIPPED, order))
        print("Order processed successfully.")


class InStoreOrderProcessor:
    def process(self, order: Order) -> None:
        print("Processing in-store order...")
        print(generate_email(ORDER_CONFIRMATION, order))
        print("Order ready for pickup.")
        print("Order processed successfully.")


def get_order_processor(order_type: OrderType) -> OrderProcessor:
    processors = {
        OrderType.ONLINE: OnlineOrderProcessor(),
        OrderType.IN_STORE: InStoreOrderProcessor(),
    }
    return processors[order_type]


def main() -> None:
    items = [
        Item(name="T-Shirt", price=Decimal("19.99")),
        Item(name="Jeans", price=Decimal("49.99")),
        Item(name="Shoes", price=Decimal("79.99")),
    ]

    online_order = Order(
        id=123, type=OrderType.ONLINE, customer_email="sarah@gmail.com"
    )

    total_price = calculate_total_price(items)
    print("Total price:", total_price)

    discounted_price = calculate_discounted_price(items, Decimal("0.1"))
    print("Discounted price:", discounted_price)

    # Process orders using the appropriate processor
    online_processor = get_order_processor(online_order.type)
    online_processor.process(online_order)

    in_store_order = Order(
        id=456, type=OrderType.IN_STORE, customer_email="john@gmail.com"
    )
    
    in_store_processor = get_order_processor(in_store_order.type)
    in_store_processor.process(in_store_order)


if __name__ == "__main__":
    main()
