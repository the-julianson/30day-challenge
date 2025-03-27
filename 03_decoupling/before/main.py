from decimal import Decimal
from stripe_service import StripePaymentService
from bank import Account, AccountType, deposit, withdraw

API_KEY = "sk_test_1234567890"

def main() -> None:
    savings_account = Account(account_number="SA001", balance=Decimal("1000"), account_type=AccountType.SAVINGS)
    checking_account = Account(account_number="CA001", balance=Decimal("500"), account_type=AccountType.CHECKING)

    payment_service = StripePaymentService()
    payment_service.set_api_key(API_KEY)

    deposit(Decimal("200"), payment_service, savings_account)
    deposit(Decimal("300"), payment_service, checking_account)

    withdraw(Decimal("100"), payment_service, savings_account)
    withdraw(Decimal("200"), payment_service, checking_account)

    print(f"Savings Account Balance: {savings_account.balance}")
    print(f"Checking Account Balance: {checking_account.balance}")


if __name__ == "__main__":
    main()
