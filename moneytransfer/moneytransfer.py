class MoneyTransferApp:
    def __init__(self):
        # In a real app, use a secure database
        self.users = {}  # username: {"password": password, "balance": balance}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists.")
            return False
        self.users[username] = {"password": password, "balance": 0}
        print(f"User {username} registered successfully.")
        return True

    def login(self, username, password):
        user = self.users.get(username)
        if not user or user['password'] != password:
            print("Invalid username or password.")
            return None
        return username

    def deposit(self, username, amount):
        self.users[username]['balance'] += amount
        print(f"Deposited ${amount}. Total balance is now ${self.users[username]['balance']}.")

    def transfer(self, sender, receiver, amount):
        if receiver not in self.users:
            print("Receiver does not exist.")
            return False
        if self.users[sender]['balance'] < amount:
            print("Insufficient balance.")
            return False
        self.users[sender]['balance'] -= amount
        self.users[receiver]['balance'] += amount
        print(f"Transferred ${amount} to {receiver}. Your new balance is ${self.users[sender]['balance']}.")
        return True

    def check_balance(self, username):
        print(f"Your balance is ${self.users[username]['balance']}.")


def main():
    app = MoneyTransferApp()
    current_user = None

    while True:
        if not current_user:
            print("\nMoney Transfer App")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter a new username: ")
                password = input("Enter a new password: ")
                app.register_user(username, password)
            elif choice == '2':
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                current_user = app.login(username, password)
            elif choice == '3':
                break
        else:
            print("\n1. Deposit Money")
            print("2. Transfer Money")
            print("3. Check Balance")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                app.deposit(current_user, amount)
            elif choice == '2':
                receiver = input("Enter receiver's username: ")
                amount = float(input("Enter amount to transfer: "))
                app.transfer(current_user, receiver, amount)
            elif choice == '3':
                app.check_balance(current_user)
            elif choice == '4':
                current_user = None

if __name__ == "__main__":
    main()
