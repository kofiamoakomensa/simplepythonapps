
# ISSUES WITH THIS VERSION 


# return statement = 
# function arguments = 
# always use break to prevent infinite loop 


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


# main entry point of the application 
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
        
        
        elif user_input in ('add', 'subtract', 'divide', 'multiply'):
            while True:
                try:
                    firstNumber = float(input("Enter first number: "))
                    secondNumber = float(input("Enter second number: "))
                    break 
                except ValueError:
                    print("Invalid number, please try again")

            if user_input == "add":
                print("The result will be ", add(firstNumber, secondNumber)) 

            elif user_input == "subtract":
                print("The result will be", subtract(firstNumber, secondNumber)) 

            elif user_input == "divide":
                print("The result will be ", divide(firstNumber, secondNumber)) 

            elif user_input == "multiply":
                print("The result will be ", multiply(firstNumber, secondNumber))

        else:
            print("Unknown input")


if __name__ == "__main__":
    main() 