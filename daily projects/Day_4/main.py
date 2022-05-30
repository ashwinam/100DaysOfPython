import random
rock = ''' rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)


computer_choice = random.choice([rock, paper, scissors])
print(f"computer choice: {computer_choice}")

if user_choice == 0 and computer_choice == scissors:
    print("You Won.")
elif computer_choice == rock and user_choice == 2:
    print("You Lose.")
elif user_choice == 2 and computer_choice == paper:
    print("You win")
elif computer_choice == scissors and user_choice == 1:
    print("You Lose.")
elif user_choice == 1 and computer_choice == rock:
    print("you win")
elif computer_choice == paper and user_choice == 0:
    print("you Lose")
else:
    print("Its an Draw.")


    