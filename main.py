class Customer:
    def __init__(self, customer_id, name, initial_balance):
        self.customer_id = customer_id
        self.name = name
        self.account = Account(initial_balance)

# Main program
if __name__ == "__main__":
    # Handle input and output here
    pass
