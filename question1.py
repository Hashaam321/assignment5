class BankAccount:
    def set_account_details(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Balance: ${self.balance}")
account = BankAccount()
account.set_account_details("123456789", "hashaam", 1000)
account.deposit(500)
account.withdraw(200)
account.display_account_info()
