#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
print(f"Hi {user_name}!")
input_string = input(f"Please, give me a string: ")
inverted_case_string = input_string.swapcase()
print(f"The inverted case of '{input_string}' is '{inverted_case_string}'")

swapped_string = ""
for char in input_string:
    new_char = char
    if char.islower():
        new_char = char.upper()
        print(f"{char} is a lowercase letter. Changing to uppercase: {new_char}")
    elif char.isupper():
        new_char = char.lower()
        print(f"{char} is an uppercase letter. Changing to lowercase: {new_char}")
    else:
        print(f"{char} is not a letter")
    swapped_string += new_char
print(f"The swapped case of '{input_string}' is '{swapped_string}'")