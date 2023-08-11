import datetime

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

# Main program
if __name__ == "__main__":
    # Handle input and output here
    pass
