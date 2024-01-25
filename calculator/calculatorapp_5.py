
# ISSUES WITH THIS 
# 

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

# function that takes users input 
def get_number(prompt):
    # while True ?? 
    while True:
        # try and exception block 
        try:
            # function argument is the input and converted to float 
            return float(input(prompt))
        except ValueError:
            print("Invalid number")




def main():
    # what is this ?? 
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
        
        # 
        elif user_input in ('1', '2', '3', '4'):
            # if first number is None ?? 
            if firstNumber is None:
                # get_number function with argument is stored in variable firstNumber 
                firstNumber = get_number("Enter the first number: ")
            if secondNumber is None: 
                secondNumber = get_number("Enter the second number: ")

            if user_input == "1":
                result = add(firstNumber, secondNumber)
            elif user_input == "2":
                result = subtract(firstNumber, secondNumber) 
            elif user_input == "3":
                result = multiply(firstNumber, secondNumber) 
            elif user_input == "4": 
                result = divide(firstNumber, secondNumber) 

            print("The result will be", result) 

            # reset the numbers for the next calculation 
            firstNumber = None 
            secondNumber = None 
        else:
            print("Unknown input. Please try again")  

        # Ask if user wants to perform another calculation 
        another_calculation = input("Do you want to perform another calculation? type(yes/no): ") 
        if another_calculation.lower() not in ("yes", "y"):
            break 

if __name__ == "__main__":
    main() 




