users = {
    "user1": {"name": "Alice", "balance": 1000, "transferred": {}},
    "user2": {"name": "Bob", "balance": 500, "transferred": {}},
}

shops = {
    "shop1": {"name": "GadgetStore", "balance": 0, "inventory": {"Gadget1": 100, "Gadget2": 200}},
    "shop2": {"name": "BookWorld", "balance": 0, "inventory": {"Book1": 50, "Book2": 75}},
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
    users[user_id]['transferred'][shop_id] = users[user_id]['transferred'].get(shop_id, 0) + amount
    return f"Transferred {amount} from {users[user_id]['name']} to {shops[shop_id]['name']}."

# Function to purchase item
def purchase_item(user_id, shop_id, item):
    if user_id not in users:
        return "User not found."
    if shop_id not in shops:
        return "Shop not found."
    if item not in shops[shop_id]['inventory']:
        return "Item not found."
    if users[user_id]['transferred'].get(shop_id, 0) < shops[shop_id]['inventory'][item]:
        return "Insufficient balance in shop account."

    users[user_id]['transferred'][shop_id] -= shops[shop_id]['inventory'][item]
    shops[shop_id]['balance'] -= shops[shop_id]['inventory'][item]
    return f"{users[user_id]['name']} purchased {item} from {shops[shop_id]['name']}."

# Function to display balances
def display_balances():
    for user_id, user_info in users.items():
        print(f"{user_info['name']} balance: {user_info['balance']}, transferred: {user_info['transferred']}")
    for shop_id, shop_info in shops.items():
        print(f"{shop_info['name']} balance: {shop_info['balance']}, inventory: {shop_info['inventory']}")

# Main command line interface
def main():
    while True:
        print("\nOptions:")
        print("1. Transfer Money")
        print("2. Purchase Item")
        print("3. Display Balances")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            shop_id = input("Enter shop ID: ")
            amount = float(input("Enter amount to transfer: "))
            print(transfer_money(user_id, shop_id, amount))
        elif choice == "2":
            user_id = input("Enter user ID: ")
            shop_id = input("Enter shop ID: ")
            item = input("Enter item to purchase: ")
            print(purchase_item(user_id, shop_id, item))
        elif choice == "3":
            display_balances()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
