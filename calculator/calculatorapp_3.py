
# ISSUES WITH THIS ?? 
# IN ASKING USERS IF THEY WANT TO CONTINUE 
# PROGRAM NEEDS TO BE SPECIFIC 
# WHAT IF I TYPE IN J. 
# WILL IT PROCESS IT AS ALSO QUIT ?? 
# IS THERE A WAY TO IMPROVE THE APP 

# ISSUE 2 
# USER HAS TO TYPE IN ALL OF STRINGS FOR IT TO WORK 
# CHANGE IT TO NUMBERS 

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
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers") 
        print("Enter 'multiply' to subtract two numbers") 
        print("Enter 'divide' to subtract two numbers") 
        print("Enter 'quit' to subtract two numbers") 
        user_input = input(": ") # what is this ?? 
        
        if user_input == "quit":
            break 
        elif user_input in ('add', 'subtract', 'multiply', 'divide'):
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


            if user_input == "add":
                result = add(firstNumber, secondNumber) 
            elif user_input == "subtract":
                result = subtract(firstNumber, secondNumber) 
            elif user_input == "multiply":
                result = multiply(firstNumber, secondNumber) 
            elif user_input == "divide":
                result = divide(firstNumber, secondNumber) 

            print("The result will be ", result) 


            # ask if the user wants to perform another calculation 
            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            # if users answer is not yes or y 
            if another_calculation.lower() not in ('yes', 'y'):
                # leave the program 
                break 
        # else unknown input try again 
        else:
            print("Unknown input. Please try again")

if __name__ == "__main__":
    main() 