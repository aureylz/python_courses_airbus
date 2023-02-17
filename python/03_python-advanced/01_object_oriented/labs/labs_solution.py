from abc import ABC, abstractmethod
from collections import namedtuple
from datetime import datetime, timedelta
import json
import logging
from time import sleep
from typing import Union
from uuid import uuid4

TransactionDetails = namedtuple('TransactionDetails', ['at_date', 'amount', 'description'])


class BankAccountBase(ABC):
    """
    This is the 'base' account class that act as a common ancestor to all account types.
    It ensures all inherited account classes will have at least those properties and methods available.
    Notice that it's marked as abstract (because it inherits from ABC).
    An abstract class is not meant to be instantiated:
    my_account = BankAccountBase('seb', 49.99) makes no sense in the real world because the bank
    has no such account type in its products catalog (only CurrentAccount, SavingAccount...).
    The child class is obliged to implement (code) the method withdraw() to cover it's specific needs.
    Because the withdraw rules will differ depending on the account type we mark it as @abstractmethod.
    Child classes can also (but are not obliged to) customize (override) the ancestor's methods to specialize them.
    """

    def __init__(self, owner: str, initial_balance: float):
        self._balance: float = 0.0
        self._owner: str = owner
        self._account_id: str = str(uuid4())
        self._created_at: datetime = datetime.now()
        self._closed_at: Union[datetime, None] = None
        self._close_reason: Union[str, None] = None
        self._transactions: list[TransactionDetails] = []
        if initial_balance > 0:
            logging.info(f'{self._owner} {type(self).__name__} created ({self._account_id}), initial balance={self._balance:,.2f}')
            self.deposit(initial_balance, 'Initial balance')
        else:
            logging.error(f'{self._owner} {type(self).__name__} creation rejected, no money provided!')
            raise ValueError("if you have no money, then you don't need a bank account...")

    def deposit(self, amount: float, description: str = None) -> float:
        """
        This methods puts money on the account.
        :param amount: the quantity of money to put on the account
        :param description: An optional description for the transaction
        :return: the new account balance
        """
        if self._closed_at is not None:
            logging.error(f'Transaction attempt on a closed account: {self._owner} tried to put {amount:,.2f} on {type(self).__name__} ({self._account_id})')
            raise PermissionError("It's forbidden to perform a transaction on a closed account")
        else:
            self._transactions.append(TransactionDetails(at_date=datetime.now(),
                                                         amount=amount,
                                                         description=description if description is not None else '<No description>'))
            self._balance += float(amount)
            logging.info(f'{self._owner} put {amount:,.2f} on {type(self).__name__} ({self._account_id}), new balance={self._balance:,.2f}')
            return self._balance

    @abstractmethod
    def withdraw(self, amount: float, description: str = None) -> float:
        """
        This methods takes money from the account.
        This abstract method is meant to be implement in the child classes (mandatory).
        This is the responsibility of the implementer to ensure the account isn't closed before performing the transaction!
        :param amount: the quantity of money to take from the account
        :param description: An optional description for the transaction
        :return: the new account balance
        """
        ...

    @property
    def history(self) -> list[TransactionDetails]:
        """
        A copy of the transactions log on the account
        :return: a list of TransactionDetails (named tuple)
        """
        logging.info(f'Audit: History request for {self._owner} {type(self).__name__} ({self._account_id})')
        result = self._transactions.copy()
        result.reverse()
        return result

    @property
    def history_fancy(self) -> str:
        """
        The transactions logs of the account plus some important account properties (balance, owner, id...)
        :return: A formatted string with the above information (suitable for printing to console)
        """
        lines: list[str] = []
        logging.info(f'Audit: History request for {self._owner} {type(self).__name__} ({self._account_id})')
        lines.extend(list(f'{k:50}:{v}' for k, v in self.details.items()))
        lines.append(f'Balance                                           :{self._balance:,.2f}')
        for transaction in self._transactions:
            if transaction.amount < 0:
                lines.append(f'{transaction.at_date:%Y-%m-%d %H:%M:%S} | {transaction.description:80} | {20 * " "} | {float(transaction.amount):>20,.2f}')
            else:
                lines.append(f'{transaction.at_date:%Y-%m-%d %H:%M:%S} | {transaction.description:80} | {float(transaction.amount):>20,.2f} |  {20 * " "}')
        return '\n'.join(lines)

    def close(self, reason: str) -> float:
        """
        Definitely closes the account
        :param reason:
        :return:
        """
        logging.info(f'{self._owner} {type(self).__name__} ({self._account_id}) is being closed')
        self._closed_at = datetime.now()
        self._close_reason = reason
        closure_balance = self._balance
        self._balance = 0
        return closure_balance

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def details(self) -> dict[str, str]:
        if self._closed_at is not None:
            return {
                'id': self._account_id,
                'owner': self._owner,
                'created_at': self._created_at,
                'closed_at': self._closed_at,
                'close_reason': self._close_reason,
            }
        else:
            return {
                'id': self._account_id,
                'owner': self._owner,
                'created_at': self._created_at,
                'balance': self._balance,
                'report_date': datetime.now(),
            }


class CurrentAccount(BankAccountBase):
    """
    This is the most used and known account type that everyone has.
    It just supports standard deposits and withdraws.
    The min balance allow (debt clearance) is 100.00 for all customers (class variable)
    """
    _debt_clearance = -100.0

    def __init__(self, owner: str, initial_balance):
        super().__init__(owner, initial_balance)

    def withdraw(self, amount: float, description: str = None) -> float:
        if self._closed_at is not None:
            logging.error(f'Transaction attempt on a closed account: {self._owner} tried to get {amount:,.2f} from {type(self).__name__} ({self._account_id})')
            raise PermissionError("It's forbidden to perform a transaction on a closed account")
        else:
            if (self._balance - amount) >= CurrentAccount._debt_clearance:
                self._transactions.append(TransactionDetails(at_date=datetime.now(), amount=-amount, description=description))
                self._balance -= amount
                logging.info(f'{self._owner} get {amount:,.2f} from {type(self).__name__} created ({self._account_id}), new balance={self._balance:,.2f}')
                return self._balance
            else:
                logging.error(f'{self._owner} cannot get {amount:,.2f} from {type(self).__name__} ({self._account_id})!')
                raise PermissionError(f'You cannot withdraw that amount of money: debt clearance exhausted !')


class SavingAccount(BankAccountBase):
    """
    This account serves a yearly interest rate.
    There's no debt clearance (the account balance remains stricly positive at any time).
    The interest rate is defined at creation and can't be changed afterwards,
    but each customer can negotiate a different rate while opening (instance variable).
    """
    def __init__(self, owner: str, initial_balance: float, interest_rate: float = .02):
        super().__init__(owner, initial_balance)
        self._interest_rate = interest_rate

    def withdraw(self, amount: float, description: str = None) -> float:
        if self._closed_at is not None:
            logging.error(f'Transaction attempt on a closed account: {self._owner} tried to get {amount:,.2f} from {type(self).__name__} ({self._account_id})')
            raise PermissionError("It's forbidden to perform a transaction on a closed account")
        if amount - self._balance < 100:
            self._transactions.append(TransactionDetails(at_date=datetime.now(), amount=-amount, description=description))
            self._balance -= amount
            logging.info(f'{self._owner} get {amount:,.2f} from {type(self).__name__} created ({self._account_id}), new balance={self._balance:,.2f}')
            return self._balance
        else:
            logging.error(f'{self._owner} cannot get {amount:,.2f} from {type(self).__name__} ({self._account_id})!')
            raise PermissionError(f'You cannot withdraw that amount of money: debt clearance exhausted!')

    def give_yearly_interests(self) -> None:
        earned_interests = self._balance * self._interest_rate
        self.deposit(earned_interests, 'Yearly interests')
        logging.debug(f'{self._owner} receives {earned_interests:,.2f} of interests on {type(self).__name__} ({self._account_id}) new balance={self._balance:,.2f}')


class CreditCardAccount(BankAccountBase):
    """
    This account allows negative balance, but in that case, the customer agrees to pay a legal 18% debt fees.
    The payments are also delayed by a certain amount of days that can be negotiated at opening.
    """
    _debt_rate = .18

    def __init__(self, owner: str, initial_balance: float, payment_delay_days: int = 30):
        super().__init__(owner, initial_balance)
        self._payment_delay_days = payment_delay_days

    def withdraw(self, amount: float, description: str = None) -> float:
        if self._closed_at is not None:
            logging.error(f'Transaction attempt on a closed account: {self._owner} tried to get {amount:,.2f} from {type(self).__name__} ({self._account_id})')
            raise PermissionError("It's forbidden to perform a transaction on a closed account")
        self._transactions.append(TransactionDetails(
            at_date=datetime.now() + timedelta(days=self._payment_delay_days),
            amount=-amount,
            description=description))
        self._balance -= amount
        logging.info(f'{self._owner} get {amount:,.2f} from {type(self).__name__} ({self._account_id}), new balance={self._balance:,.2f}')
        return self._balance

    def take_debt_fees(self) -> None:
        if self._balance < 0:
            debt_fees = -self._balance * self._debt_rate
            logging.debug(f'{self._owner} pays {debt_fees:,.2f} on {type(self).__name__} ({self._account_id}) because balance={self._balance:,.2f}')
            self.withdraw(debt_fees, 'Debt fees')


def demo_current_account(bank_name: str):
    print(f'** {bank_name} **')
    airbus_current = CurrentAccount(owner='Airbus', initial_balance=10000.0)
    sleep(1)
    airbus_current.deposit(300.0, 'Pre-sale for a plane, customer X pays 10% for booking')
    sleep(1)
    airbus_current.withdraw(15.0, 'Furniture for the factories')
    sleep(1)
    airbus_current.withdraw(37.0, 'Engine purchase')
    sleep(1)
    airbus_current.withdraw(19.0, 'Electrical fees for the factories')
    sleep(1)
    airbus_current.deposit(2700.0, 'Plane delivered, customer Y pays 90% at reception')
    print(airbus_current.history_fancy)


def demo_saving_account(bank_name: str):
    print(f'** {bank_name} **')
    my_saving_account = SavingAccount(owner='Seb', initial_balance=100.0)
    my_saving_account.give_yearly_interests()
    for month in range(12):
        my_saving_account.deposit(400.0, f'Pay day for month {month} !')
    my_saving_account.give_yearly_interests()
    my_saving_account.withdraw(2000.0, 'Buy new laptop')
    my_saving_account.withdraw(2750.0, 'Buy new loudspeakers')
    try:
        my_saving_account.withdraw(10000.0, 'Why not also buy this new fancy car?')
    except PermissionError:
        print('Argh, I would need more money to get that car!')
    my_cash = my_saving_account.close('I no longer need a saving account :)')
    print(f'I got {my_cash:,.2f} in cash!')
    try:
        my_saving_account.withdraw(100, 'Attempt to get money from a closed account :)')
    except PermissionError as ex:
        print(ex.args[0])
    print(my_saving_account.history_fancy)


def demo_credit_account(bank_name: str):
    print(f'** {bank_name} **')
    my_credit_card = CreditCardAccount(owner='Seb', initial_balance=200.0)
    try:
        # Try to get interest from this account type, who knows, it might work...
        my_credit_card.give_yearly_interests()
    except AttributeError as ex:
        print(ex.args[0])
    my_credit_card.withdraw(6.35, 'Canteen')
    my_credit_card.withdraw(189.0, 'Beers with the tam')
    my_credit_card.withdraw(120.0, 'Fuel for the car')
    try:
        my_credit_card.withdraw(10000.0, "With that account I can get that car, but I'll pay massive debt fees...")
    except PermissionError:
        # that cannot happen because CreditCardAccount allows the payment
        # even if the balance isn't sufficient to cover the purchase...
        pass
    my_credit_card.take_debt_fees()
    print(my_credit_card.history_fancy)


if __name__ == '__main__':
    # Change me to see more verbose logs !
    # logging.basicConfig(level=logging.DEBUG)
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.WARNING)

    # Challenge for the bravest...
    # In this version, we trust the implementers of the child classes enough.
    # But, a faulty implementation could possibly (real bug or bad guys):
    # - withdraw money from a closed account...
    # - update or delete existing transactions from the history...
    # To prevent those attacks, in the base class:
    # - turn the self._transactions from protected to private: self.__transactions (a __ prefix means private)
    # - add a protected method so that child classes can ONLY append a transaction to your private self.__transactions
    demo_saving_account('My Online Bank')
    demo_credit_account('My Credit Card')
    demo_current_account('European Central Bank')
