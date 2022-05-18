



#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

num1 = int(input("What is your first number?: "))
print("\n")
for symbol in operations:
    print (symbol)
print("\n")
user_operation = input("What operation would you like to use from above: ")
num2 = int(input("\nWhat is your second number?: "))

# Old if statement
# if user_operation == "+":
#   answer = num1 + num2
# elif user_operation == "-":
#   answer = num1 - num2
# elif user_operation == "*":
#   answer = num1 * num2
# else:
#   answer = num1 / num2

print(f"{num1} {user_operation} {num2} = {answer}")
    