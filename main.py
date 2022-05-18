#Calculator
from art import logo
#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2
#Exponent
def exponent(n1, n2):
  return n1 ** n2

#Dictionary of Operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": exponent,
}
def calculator():
  print(logo)
  num1 = float(input("\nWhat is your first number?: "))
  print("\n")
  for symbol in operations:
      print (symbol)
  print("\n")
  using_calculator = True
  
  while using_calculator is True:
    user_symbol = input("Pick an operation: ")
    num2 = float(input("\nWhat is the next number?: "))
    calculation_function = operations[user_symbol]
    answer = calculation_function(num1, num2)
    print(f"\n{num1} {user_symbol} {num2} = {answer}\n")
    user_response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
    if user_response == "y":
      num1 = answer
      print(f"The current answer is {answer}")
    else:
      using_calculator = False
      calculator()

calculator()
    
    