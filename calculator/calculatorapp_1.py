
# ISSUES WITH THIS VERSION 
# WHEN USER TYPES IN AN ALPHABET IN SECOND ENTRY 
# EXCEPTION THROWS BUT IT TAKES USER BACK TO FIRST ENTRY 

# add function 
def add(x, y):
    return x + y 


# subtract function 
def subtract(x, y):
    return x - y 

# multiply function 
def multiply(x, y):
    return x * y 

# divide function 
def divide(x, y):
    # if the denominator is zero then throw an error 
    if y == 0:
        return "Error! Division by zero" 
    # else compute the division 
    return x / y 


# main entry point of the application 
def main():
    # why while true ?? 
    while True:
        # print statements 
        print("\nOptions:") 
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers") 
        print("Enter 'multiply' to subtract two numbers") 
        print("Enter 'divide' to subtract two numbers") 
        print("Enter 'quit' to subtract two numbers") 
        
        # what is this ?? 
        user_input = input(": ") 
        
        # if user types in quit string 
        # then leave the program 
        if user_input == "quit":
            break 
        
        # if users input is either add, subtract, divide, multiply 
        elif user_input in ('add', 'subtract', 'divide', 'multiply'):
            # what is while True ?? 
            while True:
                # why using exception handling here ?? 
                try:
                    # ask for first number and take number 
                    firstNumber = float(input("Enter first number: "))
                    # ask for second number and take second number 
                    secondNumber = float(input("Enter second number: "))
                    # after leave the loop 
                    break 
                # throw the ValueError if users answers are not numbers 
                except ValueError:
                    # print a statement to the user 
                    print("Invalid number, please try again")
            
            # if user types add 
            if user_input == "add":
                # print a statement to the user and calling the add function created 
                print("The result will be ", add(firstNumber, secondNumber)) 
            # if user types in subtract 
            elif user_input == "subtract":
                # do the same as above 
                print("The result will be", subtract(firstNumber, secondNumber)) 

            elif user_input == "divide":
                print("The result will be ", divide(firstNumber, secondNumber)) 

            elif user_input == "multiply":
                print("The result will be ", multiply(firstNumber, secondNumber))
        
        # else if user does not type in any of these then print to user unknown input 
        else:
            print("Unknown input")

# this makes the script work 
if __name__ == "__main__":
    main() 