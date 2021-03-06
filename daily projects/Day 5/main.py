#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 

# random_letters = random.sample(letters, nr_letters)


# nr_symbols = int(input(f"How many symbols would you like?\n"))

# random_symbols = random.sample(symbols, nr_symbols)

# nr_numbers = int(input(f"How many numbers would you like?\n"))

# random_numbers = random.sample(numbers, nr_numbers)


# password = random_letters + random_symbols + random_numbers
# # before shuffle
# print(password)
# # after shuffle
# random.shuffle(password)
# print(password)
# print(f"your password is: {''.join(password)}")


# other way
# Easy way

if __name__ == "__main__":
  print("Welcome to the PyPassword Generator!")
  
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  
  
  # password = ""
  # # letter
  # for letter in range(1, nr_letters + 1):
  #   password += random.choice(letters)
  
  # # symbol
  # for symbol in range(1, nr_symbols + 1):
  #   password += random.choice(symbols)
  
  # # numbers
  # for number in range(1, nr_numbers + 1):
  #   password += random.choice(numbers)
  
  # print(password)
  
  # hard way
  password_list = []
  for letter in range(1, nr_letters + 1):
    password_list += random.choice(letters)
  
  # symbol
  for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
  
  # numbers
  for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
  
  # print(password_list)
  random.shuffle(password_list)
  # print(password_list)
  
  password = ""
  for password_char in password_list:
    password += password_char
  
  print("Your Password is: ", password)