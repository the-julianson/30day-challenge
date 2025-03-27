import pytest
from ..bank import Account, AccountType, deposit, withdraw
from decimal import Decimal
from unittest.mock import Mock

def test_account_deposit_updates_balance():
    account = Account(account_number="123456789", account_type=AccountType.CHECKING, balance=Decimal("100"))
    account.deposit(Decimal("50"))
    assert account.balance == Decimal("150")

def test_account_withdraw_updates_balance():
    account = Account(account_number="1234", account_type=AccountType.SAVINGS, balance=Decimal("1000"))
    account.withdraw(Decimal("200"))
    assert account.balance == Decimal("800")

def test_deposit_function_calls_payment_and_account_deposit():
    payment_mock = Mock()
    account = Account(account_number="SX120", account_type=AccountType.CHECKING, balance=Decimal("500"))
    deposit(Decimal("50"), payment_mock, account)
    payment_mock.process_payment.assert_called_once_with(Decimal("50"))
    assert account.balance == Decimal("550")

def test_withdraw_function_calls_payment_and_account_deposit():
    payment_mock = Mock()
    account = Account(account_number="SX120", account_type=AccountType.CHECKING, balance=Decimal("500"))
    withdraw(Decimal("50"), payment_mock, account)
    payment_mock.process_payout.assert_called_once_with(Decimal("50"))
    assert account.balance == Decimal("450")