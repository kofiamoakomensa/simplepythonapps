# Hardcoded list of professionals
professionals = [
    {"name": "John Doe", "expertise": "Finance", "fee": 100},
    {"name": "Jane Smith", "expertise": "Marketing", "fee": 80},
    {"name": "Alice Johnson", "expertise": "Software Development", "fee": 120}
]

def list_professionals():
    print("\nAvailable Professionals:")
    for idx, prof in enumerate(professionals, 1):
        print(f"{idx}. {prof['name']} - Expertise: {prof['expertise']}, Fee: ${prof['fee']}")

def request_advice(professional_index):
    professional = professionals[professional_index - 1]
    print(f"\nYou have selected {professional['name']} for advice in {professional['expertise']}.")
    print(f"The fee for the advice is ${professional['fee']}.")
    # Simulate payment (in a real application, integrate a payment system here)
    print("Processing payment...")
    print("Payment successful!\n")
    # Simulate providing advice
    print(f"{professional['name']} says: 'Here is my professional advice on {professional['expertise']}.'")

def main():
    while True:
        print("\nWelcome to the Professional Advice App")
        list_professionals()
        choice = input("Choose a professional by number (or 'exit' to quit): ")
        if choice.lower() == 'exit':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(professionals):
            request_advice(int(choice))
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
