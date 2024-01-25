
# USING LAMBDA FUNCTIONS INSTEAD 
def get_number(prompt):
    while True:
        try: 
            return float(input(prompt)) 
        except ValueError:
            print("Invalid number") 


def main(): 
    # lambda functions for arithmetic operations 
    # what is the difference between lambda vs normal functions ?? 
    add = lambda x, y: x + y 
    subtract = lambda x, y: x - y 
    multiply = lambda x, y: x * y 
    divide = lambda x, y: "Error! Division by zero" if y == 0 else x / y 

    firstNumber = None 
    secondNumber = None 


    while True:
        print("\nOptions:") 
        print("Enter '1' to add two numbers")
        print("Enter '2' to subtract two numbers") 
        print("Enter '3' to multiply two numbers") 
        print("Enter '4' to divide two numbers") 
        print("Enter 'quit' to exit the program") 
        user_input = input(": ") 

        if user_input == "quit":
            break 

        elif user_input in ('1', '2', '3', '4'):
            if firstNumber is None: 
                firstNumber = get_number("Enter first number: ")
            if secondNumber is None: 
                secondNumber = get_number("Enter second number: ")

            operation = {"1": add, "2": subtract, "3": multiply, "4": divide}.get(user_input) 
            result = operation(firstNumber, secondNumber) if operation else "invalid operation" 

            print("The result will be", result)

            firstNumber = None 
            secondNumber = None 
        else:
            print("Unknown input, Please try again")

        another_calculation = input("Do you want to perform another calculation? type(yes/no): ")
        if another_calculation.lower() not in ("yes", "y"):
            break 

if __name__ == "__main__":
    main() 