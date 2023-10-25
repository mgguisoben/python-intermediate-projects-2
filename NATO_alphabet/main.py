import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {alpha.letter : alpha.code for _, alpha in data.iterrows()}

user_input = input("Enter a word: ").upper()

alpha_list = [alpha_dict[letter] for letter in user_input]

print(alpha_list)