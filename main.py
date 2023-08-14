import datetime
import random

class Customer:
    def __init__(self, customer_id, name, initial_balance):
        self.__customer_id = customer_id
        self.__name = name
        self.__account = Account(initial_balance)

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_account(self):
        return self.__account

class Account:
    def __init__(self, initial_balance):
        self.__account_id = generate_account_id()  # Private method to generate account ID
        self.__balance = initial_balance
        self.__transactions = []

    def __add_transaction(self, transaction):
        self.__transactions.append(transaction)
        if len(self.__transactions) > 10:
            self.__transactions.pop(0)

    def withdraw(self, amount):
        return BankModule.withdraw(self, amount)

    def deposit(self, amount):
        return BankModule.deposit(self, amount)

    def transfer(self, destination_account, amount):
        return BankModule.transfer(self, destination_account, amount)

    def get_balance(self):
        return self.__balance

    def last_10_transactions(self):
        return self.__transactions

    def get_account_id(self):
        return self.__account_id


class BankModule:
    @staticmethod
    def withdraw(account, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if account.get_balance() - amount < 0:
            return "Insufficient funds."
        transaction = Transaction(amount, 'Debit', account.get_balance() - amount, 'Withdrawal')
        account._Account__balance -= amount
        account._Account__add_transaction(transaction)
        return transaction

    @staticmethod
    def deposit(account, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        transaction = Transaction(amount, 'Credit', account.get_balance() + amount, 'Deposit')
        account._Account__balance += amount
        account._Account__add_transaction(transaction)
        return transaction

    @staticmethod
    def transfer(source_account, destination_account, amount):
        if amount <= 0:
            return "Invalid transfer amount."
        if source_account.get_balance() - amount < 0:
            return "Insufficient funds for transfer."
        transaction = Transaction(amount, 'Debit', source_account.get_balance() - amount, f'Transfer to {destination_account.get_account_id()}')
        destination_transaction = Transaction(amount, 'Credit', destination_account.get_balance() + amount, f'Transfer from {source_account.get_account_id()}')
        source_account._Account__balance -= amount
        destination_account._Account__balance += amount
        source_account._Account__add_transaction(transaction)
        destination_account._Account__add_transaction(destination_transaction)
        return transaction

    @staticmethod
    def show_balance(account):
        return account.get_balance()

    @staticmethod
    def last_10_transactions(account):
        return account.last_10_transactions()

class Transaction:
    def __init__(self, amount, transaction_type, available_balance, description):
        self.__transaction_id = generate_transaction_id()  # Private method to generate transaction ID
        self.__amount = amount
        self.__transaction_type = transaction_type
        self.__available_balance = available_balance
        self.__description = description
        self.__date = datetime.datetime.now()

    def get_transaction_id(self):
        return self.__transaction_id

    def get_amount(self):
        return self.__amount

    def get_transaction_type(self):
        return self.__transaction_type

    def get_available_balance(self):
        return self.__available_balance

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date.strftime('%Y-%m-%d %H:%M:%S')

def generate_10_digit_number():
    return random.randint(10**9, 10**10 - 1)

def generate_account_id():
    # Implement a unique account ID generator logic
    return generate_10_digit_number()

def generate_transaction_id():
    # Implement a unique transaction ID generator logic
    return generate_10_digit_number()


class Database:
    def __init__(self):
        self.__users = {}

    def login(self):

        en =""

        while en!='1' and en!='2':
            en = input("1. Existing User\n2. New User\n>").strip()

        if en == 1:
            customer_id = input("Enter your customer ID: ")
            password = input("Enter your password: ")
            user = self.__users.get(customer_id)
            if user is None:
                print("User not found.\nAlert: System Closing!")
                return
            if password == user['password']:
                print("Login successful.")
                return user['customer']
            else:
                print("Incorrect password.")
                return None
        else:
            return self.__create_user(generate_account_id())

    def __create_user(self, customer_id):
        name = input("Enter your name: ")
        initial_balance = "P"
        # while not initial_balance.isdigit():
        initial_balance = float(input("Enter initial balance: "))

        password = input("Create a password: ")

        customer = Customer(customer_id, name, initial_balance)
        self.__users[customer_id] = {'customer': customer, 'password': password}

        print("User created successfully.")
        return {'customer': customer, 'password': password}


# Main program
if __name__ == "__main__":
    bank_database = Database()
    finalBreak = False
    while not finalBreak:
        user = bank_database.login()
        while True:
            options = [
                "Show Balance",
                "Withdraw Money",
                "Deposit Money",
                "Transfer Funds",
                "Display Last 10 Transactions",
                "Log Out",
                "Quit"
            ]

            print(f"Welcome, {user['customer'].get_name()}!\n\n")
            for i in range(len(options)):
                print(f'{i+1}. {options[i]}\n')
            inp = "0"
            while not 0<int(inp)<8:
                inp = input("\nEnter your option [1-7] :").strip()

            if inp=='7':
                finalBreak = True
                break
            elif inp == '6':
                break
            elif inp == '1':
                print(f"You Current Balance is {user['customer'].get_account.get_balance}")



        # Handle banking operations here using the BankModule
