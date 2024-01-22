
# ISSUES WITH THIS 
# IS THERE A WAY TO IMPROVE THE APP 

def add(x, y):
    return x + y 


def subtract(x, y):
    return x - y 


def multiply(x, y):
    return x * y 


def divide(x, y):
    if y == 0:
        return "Error! Division by zero" 
    return x / y 


def main(): 
    while True:
        print("\nOptions:") 
        print("Enter '1' to add two numbers")
        print("Enter '2' to subtract two numbers") 
        print("Enter '3' to subtract two numbers") 
        print("Enter '4' to subtract two numbers") 
        print("Enter 'quit' to subtract two numbers") 
        user_input = input(": ") # what is this ?? 
        
        if user_input == "quit":
            break 
        elif user_input in ('1', '2', '3', '4'):
            while True:
                try:
                    firstNumber = float(input("Enter first number: "))
                    break 
                except ValueError:
                    print("Invalid Input. Please enter a valid first number")

            while True:
                try:
                    secondNumber = float(input("Enter second number: "))
                    break 
                except ValueError:
                    print("Invalid Input. Please enter a valid second number")


            if user_input == "1":
                result = add(firstNumber, secondNumber) 
            elif user_input == "2":
                result = subtract(firstNumber, secondNumber) 
            elif user_input == "3":
                result = multiply(firstNumber, secondNumber) 
            elif user_input == "4":
                result = divide(firstNumber, secondNumber) 

            print("The result will be ", result) 


            # ask if the user wants to perform another calculation 
            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation.lower() not in ('yes', 'y'):
                break 
        else:
            print("Unknown input. Please try again")

if __name__ == "__main__":
    main() 