import random

class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True
        self.is_bankrupt = False

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(1000, 9999)
        user = User(account_number, name, email, address, account_type)
        self.users.append(user)
        return user

    def delete_account(self, user):
        self.users.remove(user)

    def get_user_by_account_number(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None

    def get_all_accounts(self):
        return self.users

    def check_bank_balance(self):
        return self.total_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def loan_on_off(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        return self.loan_feature_enabled
    
    def bankruptcy_on_off(self, info):
        if info == "yes":
            self.is_bankrupt = True
            print("Bankrupt feature enabled.")
        elif info == "no":
            self.is_bankrupt = False
            print("Bankrupt feature disabled.")
        else:
            print("Wrong keyword")
        


class User:

    def __init__(self, account_number, name, email, address, account_type):
        self.account_number = account_number
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):

        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount, bank):
        if bank.loan_feature_enabled and self.loan_taken < 2:
            self.balance += amount
            self.loan_taken += 1
            bank.total_loan_amount += amount
            self.transaction_history.append(f"Loan taken: {amount}")
        else:
            print("limit reached.")

    def transfer(self, amount, recipient):
        if recipient is not None:
            if amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Recipient account does not exist.")


def main():
    bank = Bank()

    while True:
        print("1. Create an account for new user ")
        print("2. User")
        print("3. Admin")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings/Current): ").capitalize()
            new_user = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully. Account number: {new_user.account_number}")

        elif choice == "2":
            user_menu(bank)

        elif choice == "3":
            admin_menu(bank)

        elif choice == "4":
            print("Exiting the banking system. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


def user_menu(bank):
    print("\nUser Menu:")
    account_number = int(input("Enter your account number: "))
    user = bank.get_user_by_account_number(account_number)

    if user:
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Take Loan")
            print("6. Transfer Money")
            print("7. Back to Main Menu")

            user_choice = input("Enter your choice (1-7): ")

            if user_choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                user.deposit(amount)

            elif user_choice == "2":

                if bank.is_bankrupt == True :
                    print("Bank is bankrupt")
                else :
                    amount = float(input("Enter the amount to withdraw: "))
                    user.withdraw(amount)

            elif user_choice == "3":
                balance = user.check_balance()
                print(f"Available Balance: {balance}")

            elif user_choice == "4":
                history = user.check_transaction_history()
                print("Transaction History:")
                for transaction in history:
                    print(transaction)

            elif user_choice == "5":
                if bank.loan_feature_enabled:
                    amount = float(input("Enter the loan amount: "))
                    user.take_loan(amount, bank)
                else:
                    print("Loan feature is currently disabled.")

            elif user_choice == "6":
                recipient_account_number = int(input("Enter recipient's account number: "))
                recipient = bank.get_user_by_account_number(recipient_account_number)
                user.transfer(float(input("Enter the amount to transfer: ")), recipient)

            elif user_choice == "7":
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    else:
        print("User not found.")


def admin_menu(bank):
    print("\nAdmin Menu:")
    while True:
        print("\n1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Check Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Loan Feature ON/OFF")
        print("7. Bank bankruptcy feature ON/OFF")
        print("8. Back to Main Menu")

        admin_choice = input("Enter your choice (1-8): ")

        if admin_choice == "1":
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings/Current): ").capitalize()
            new_user = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully. Account number: {new_user.account_number}")

        elif admin_choice == "2":
            account_number = int(input("Enter the account number to delete: "))
            user = bank.get_user_by_account_number(account_number)
            if user:
                bank.delete_account(user)
                print("Account deleted successfully.")
            else:
                print("Account not found.")

        elif admin_choice == "3":
            all_accounts = bank.get_all_accounts()
            print("All User Accounts:")
            for user in all_accounts:
                print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.balance}")

        elif admin_choice == "4":
            bank_balance = bank.check_bank_balance()
            print(f"Total Bank Balance: {bank_balance}")

        elif admin_choice == "5":
            loan_amount = bank.check_total_loan_amount()
            print(f"Total Loan Amount: {loan_amount}")

        elif admin_choice == "6":
            loan_feature_status = "enabled" if bank.loan_feature_enabled else "disabled"
            print(f"Loan feature is currently {loan_feature_status}")
            new_status = input("Do you want to on/off the loan feature of the bank? (yes/no): ").lower()
            if new_status == "yes":
                loan_feature_status = "enabled" if bank.loan_on_off() else "disabled"
                print(f"Loan feature is now {loan_feature_status}")

        elif admin_choice == "7":
            print(f"Bankrupt feature is currently {bank.is_bankrupt}")
            new_status = input("Type -yes- to on bankrupt feature and -no- to off: ").lower()
            bank.bankruptcy_on_off(new_status)

        elif admin_choice == "8":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
