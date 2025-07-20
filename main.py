import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    words = input("Type a word for conversation: ").upper()
    try:
        output_list= [phonetic_dict[letter] for letter in words]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

