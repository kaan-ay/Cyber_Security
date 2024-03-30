from random import choice
from string import ascii_letters

original_message = input('Please enter the message you would like encoded.\n')
encoded_message = []
mappings = dict()

for letter in set(original_message):
    new_letter = choice(list(ascii_letters) + [" "])
    while new_letter in mappings.keys():
        new_letter = choice(list(ascii_letters) + [" "])
    mappings[letter] = new_letter

for letter in original_message:
    encoded_message.append(mappings[letter])


print(" ".join(encoded_message))
print(mappings)
