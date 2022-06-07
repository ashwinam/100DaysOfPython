# import art
# import random

# #Number Guessing Game Objectives:

# # Include an ASCII art logo.
# # Allow the player to submit a guess for a number between 1 and 100.
# # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# # If they got the answer correct, show the actual answer to the player.
# # Track the number of turns remaining.
# # If they run out of turns, provide feedback to the player. 
# # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


# """
# To-Do's for project
# 1. Logo --> done
# 2. title "Welcome to the number guessing game!" ---> done
# 3. input for user(select difficuly) "Choose a Difficulty. type 'easy' or 'hard' --> "easy" get 10 attempts and "hard" get 5 attempts".
# 4. show the attempts based on difficulty
#   i. ask the user "make a guess" for the number
#   ii. if guess > random number " Too high Guess again. "
# elif guess < random number " Too low Guess again. "
#   iii. after each attempt less by 1 attempts, if 5 attempts the next it have only 4 attempts
#   iv. if you guess it right " you got it right the answer was <number>"
#   v. exit
# """

# print(art.logo)
# print("Welcome to the number guessing game!")
# print("The range of numbers between is 1 and 100")

# number_to_be_guessed = random.randint(1, 100)
# print(f"the random number is {number_to_be_guessed}")

# difficulty = input("Choose a Difficulty. type 'easy' or 'hard': ")

# if difficulty == "easy":
#   remaining_guesses = 10
# else:
#   remaining_guesses = 5

# game_not_over = True
# while remaining_guesses > 0  and game_not_over:
#   print(f"You have {remaining_guesses} attempts remaining to guess the number.")
#   guess = int(input("Make a Guess. "))
#   if guess > number_to_be_guessed:
#     print("Too High. \nGuess again.")
#   elif guess < number_to_be_guessed:
#     print("Too Low. \nGuess again.")
#   else:
#     game_not_over = False
#     print(f"You got it right. The answer was {number_to_be_guessed}")
#   remaining_guesses -= 1




# Angela code
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()