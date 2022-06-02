import random
import hangman_words
import hangman_art

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
# Testing purpose
print(f"The word is {chosen_word}")

lives = 6

display = []
for _ in range(len(chosen_word)):
  display.append("_")

end_of_game = False


while not end_of_game:
  guess = input("Enter your word: ").lower()
  
  if guess in display:
    print(f"You have already guessed {guess}.")
    
  for index, word in enumerate(chosen_word):
    if guess == word:
      display[index] = word

  
  if guess not in chosen_word:
    lives -=1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
      end_of_game = True
      print("You Lose.")
    
  print(f'{" ".join(display)}')
 
  print(hangman_art.stages[lives])
  
  if "_" not in display:
    end_of_game = True
    print("You Win.")

  