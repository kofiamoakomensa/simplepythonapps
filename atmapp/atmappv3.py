class ATM:
    def __init__(self):
        self.balance = 0
        self.full_name = None
        self.password = None

    def setup_account(self, full_name, password):
        self.full_name = full_name
        self.password = password
        print(f"Account created for {self.full_name}.")

    def check_credentials(self, full_name, password):
        return self.full_name == full_name and self.password == password

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            print("Here is your updated balance:")
            self.check_balance()

def main():
    atm = ATM()
    print("Welcome to the ATM")
    full_name = input("Enter your full name for account setup: ")
    password = input("Create a password for your account: ")
    atm.setup_account(full_name, password)

    # sign in process 
    while True:
        print("\nPlease sign in to your account.")
        sign_in_name = input("Enter your fullname: ")
        sign_in_password = input("Enter your password: ")
        if atm.check_credentials(sign_in_name, sign_in_password):
            break 
        else: 
            print("Invalid credentials. Please try again")

    while True:
        print("\nATM Menu")
        print("1 - Check Balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            atm.deposit()
        elif choice == '3':
            atm.withdraw()
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
