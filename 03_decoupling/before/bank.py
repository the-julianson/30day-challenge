from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol
from enum import StrEnum, auto


class PaymentService(Protocol):

    def set_api_key(self, api_key: str) -> None:
        ...

    def process_payment(self, amount: Decimal) -> None:
        ...

    def process_payout(self, amount: Decimal) -> None:
        ...

# From this 
class AccountType(StrEnum):
    SAVINGS = auto()
    CHECKING = auto()

@dataclass
class Account:
    account_number: str
    balance: Decimal
    account_type: AccountType

    def deposit(self, amount: Decimal) -> None:
        print(f"Depositing {amount} into {self.account_type} Account {self.account_number}")
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        print(f"Withdrawing {amount} from {self.account_type} Account {self.account_number}")
        self.balance -= amount


def deposit(
    amount: Decimal, payment_service: PaymentService, account: Account
) -> None:
    payment_service.process_payment(amount)
    account.deposit(amount=amount)
    # payment_service.set_api_key("sk_test_1234567890")
    

def withdraw(
    amount: Decimal, payment_service: PaymentService, account: Account
) -> None:
    payment_service.process_payout(amount)
    account.withdraw(amount=amount)
    
