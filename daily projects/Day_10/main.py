# Calculator

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations_dict = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}


num1 = int(input("What's the first number? "))

# retrive the keys from dictionery
for keys in operations_dict:
  print(keys)

operations_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number? "))

function = operations_dict[operations_symbol]
answer = function(num1, num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")