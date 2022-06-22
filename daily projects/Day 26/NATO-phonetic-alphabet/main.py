import pandas


# TODO 1. Create a dictionary in this format:

alphabets_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabets_dict = {row.letter: row.code for index, row in alphabets_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_name = list(input("Enter the word: ").upper())

nato_alphabet_output = [nato_alphabets_dict[word] for word in user_name]
print(nato_alphabet_output)
