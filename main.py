from replit import clear
from art import logo

print(logo)

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

Operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():

  should_continue = True

  num1 = float(input("What's the first number ?"))

  for symbols in Operations:
    print(symbols)

  while should_continue:
     operation_symbol = input("Pick an operation: ")
     num2 = float(input("What's the second number ?"))

     calculation_function = Operations[operation_symbol]
     result = calculation_function(num1,num2)

     print(f"{num1} {operation_symbol} {num2} = {result}")
     further_operation = input(f"Type 'y' to continue calculating with {result} , 'n' to start new operation or any other thing to close.")

     if further_operation == "y":
       num1 = result
     elif further_operation == "n":
        should_continue = False
        clear()
        calculator()
     else:
       should_continue = False

calculator()

    
    
        

     


