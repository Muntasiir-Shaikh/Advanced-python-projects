
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print("Balance =", self.balance)
            print("Deposite successfully")
        else:
            print("Invalid deposite")

    def withdraw(self, withdraw):
        if withdraw <= 0:
            print("Invalid withdraw amount")

        elif withdraw <= self.balance:
            print("Available Balance =", self.balance)
            self.balance -= withdraw
            print("Withdraw successfully")
            print("Updated Balance =", self.balance)

        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Checking balance =", self.balance)

    def account_details(self):
        print("Account Holder =", self.name)
        print("Current Balance =", self.balance)


account1 = BankAccount("Preeti", 5000)
account2 = BankAccount("Rahul", 3000)


while True:

    print("\n------- Select Account -------")
    print("1. Preeti")
    print("2. Rahul")
    print("3. Exit")

    a = input("Enter a no: ")

    if a == "1":
        selected_account = account1

    elif a == "2":
        selected_account = account2

    elif a == "3":
        print("Thank you for using Banking System")
        break

    else:
        print("Invalid selection")
        continue

    while True:

        print("\n------- Banking Management System -------")
        print("1. Deposite Amount")
        print("2. Withdraw Amount")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Back")

        n = input("Enter a no: ")

        if n == "1":
            amount = int(input("Enter the deposite amount: "))
            selected_account.deposite(amount)
            break

        elif n == "2":
            amount = int(input("Enter withdraw amount: "))
            selected_account.withdraw(amount)
            break

        elif n == "3":
            selected_account.check_balance()
            break

        elif n == "4":
            selected_account.account_details()
            break

        elif n == "5":
            break

        else:
            print("Enter a no between 1 to 5")

# selected_account.deposite(amount)
# selected_account.withdraw(amount)
# selected_account.check_balance()
# selected_account.account_details()

# account1.account_details()
# account2.account_details()

# account1.deposite(1000)
# account1.withdraw(2000)

# account1.check_balance()
# account2.check_balance()

# BankAccount.check_balance(account1)

# print(account1.name , account1.balance)
# print(account2.name , account2.balance)


