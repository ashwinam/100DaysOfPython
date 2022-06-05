import art

# logo
print(art.logo)


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

def calculation():
  num1 = float(input("What's the first number? "))
  
  # retrive the keys from dictionery
  for keys in operations_dict:
    print(keys)
  
  should_continue = True
  
  while should_continue:
  
    operations_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    
    function = operations_dict[operations_symbol]
    answer = function(num1, num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")
  
    if input(f'type "y" to continue with {answer}, or type "n" to start a new calculation:  ') == "y":
      num1 = answer
    else:
      should_continue = False
      calculation()

calculation()
  







# operations_symbol = input("Pick an operation: ")
  
#   num3 = int(input("What's the third number? "))
  
#   function = operations_dict[operations_symbol]
  
#   # second_answer = function(function(num1, num2), num3) # bug
  
#   second_answer = function(first_answer, num3)
  
#   print(f"{first_answer} {operations_symbol} {num3} = {second_answer}")