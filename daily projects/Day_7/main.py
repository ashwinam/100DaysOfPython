import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


display = []
for _ in range(len(chosen_word)):
  display.append("_")

print(display)


while "_" in display:
  guess = input("Enter your word: ").lower()
  
  for index, word in enumerate(chosen_word):
    if guess == word:
      display[index] = word
  
  print(display)
else:
  print("You Win.")