# User and Shop Data (Hardcoded)
users = {
    "user1": {"name": "Alice", "balance": 1000},
    "user2": {"name": "Bob", "balance": 500},
}

shops = {
    "shop1": {"name": "GadgetStore", "balance": 2000},
    "shop2": {"name": "BookWorld", "balance": 3000},
}

# Function to transfer money
def transfer_money(user_id, shop_id, amount):
    if user_id not in users:
        return "User not found."
    if shop_id not in shops:
        return "Shop not found."
    if users[user_id]['balance'] < amount:
        return "Insufficient balance."
    
    users[user_id]['balance'] -= amount
    shops[shop_id]['balance'] += amount
    return f"Transferred {amount} from {users[user_id]['name']} to {shops[shop_id]['name']}."

# Function to display balances
def display_balances():
    for user_id, user_info in users.items():
        print(f"{user_info['name']} balance: {user_info['balance']}")
    for shop_id, shop_info in shops.items():
        print(f"{shop_info['name']} balance: {shop_info['balance']}")

# Main command line interface
def main():
    while True:
        print("\nOptions:")
        print("1. Transfer Money")
        print("2. Display Balances")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            shop_id = input("Enter shop ID: ")
            amount = float(input("Enter amount to transfer: "))
            print(transfer_money(user_id, shop_id, amount))
        elif choice == "2":
            display_balances()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
