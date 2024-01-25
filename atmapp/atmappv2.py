# ISSUES 
# ACCOUNT SIGN UP 



class ATM:
    def __init__(self):
        self.balance = 0

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
            print("Here is your updated balance: ")
            self.check_balance() 

def main():
    atm = ATM()
    while True:
        print("\nATM")
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