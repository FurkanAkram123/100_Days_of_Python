from ASCII_Art import logo
import numpy as np
print (logo[0])
print ("Welcome to the calculator!")
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    
    return np.round(n1 / n2,2)  

#place all functions in a dictionary
all_operations = { 
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide 
                  }

num1 = float(input("What's the first number?: "))

while True:
    
    operation_required = input(str(f"Pick an operation: {all_operations.keys()}"))

    #check if the operation is valid
    if operation_required not in all_operations:
        print ("Invalid operation. Please try again.")
        continue

    num2 = float(input("What's the second number?: "))

    #print the entire calculation
    print (num1, operation_required, num2, "=", all_operations[operation_required](num1, num2))
    num1 = all_operations[operation_required](num1, num2)

    #check if the user wants to continue
    if (input("Do you want to continue (y/n)") == "n"):
        print ("Thank you for using the calculator!")
        break


