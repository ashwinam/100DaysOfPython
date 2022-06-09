# """My borken code """

# # Welcome to the Higher Lower Game.

# """
# Game Requirements for building stuffs
# 1.when the game start first it appear logo
# 2.in compare A: it pick random data from game data file
# 3. vs logo
# 4. Against B: random data
# 5. input type answer from a and b
#   a. correct then it appears your right and it appears top after logo and it generate a score (counter)
#   b. wrong answer end the game and return total score.
# 6. every time it clear the screen
# """

# # Tasks
# # 1. import the Logo [done]
# import art
# print(art.logo)



# # 2. generate a random number for extracting the data from game data [done]
# import random
# from game_data import data

# def generate_question(data):
#   random_number = random.randint(0, len(data)-1)
#   question = data[random_number]
#   return question
    

# # print(generate_question(data))


# # 3. use random number to collect the random data for A & B. [done]

# question_a = generate_question(data)
# question_b = generate_question(data)
# # print(f"Compare A:{question_a}")
# # print(f"Compare B{question_b}")



# # 4. vs logo in between questions[done]
# print(art.vs)


# # extract the data from dictionary[done]
# def extracting_data(dictionary):
#   data = []
#   final_data = []
#   for key in dictionary:
#     data.append(dictionary[key])
#   final_data.append(f"{data[0]}, a {data[2]}, from {data[3]}")
#   final_data.append(data[1])
#   return final_data
  
    
# print(extracting_data(question_a))
# print(extracting_data(question_b))



# # 5. input and compare the answer
# get_input = input("Who has more followers? Type 'A' and 'B': ").upper()
# print(get_input)

# # comparing the answers

# def compare(input):
#   if input == "A":
#     a = extracting_data(question_a)[1]
#   else:
#     b = extracting_data(question_b)[1]

  

# # 6. score appear on after logo if it is more than 0
# # 7. aswer correct then it continues 
# # 8. wrong anser end the game and shows the score



# Angelas Code


from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''



# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.