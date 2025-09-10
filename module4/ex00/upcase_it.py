#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
word_input = input(f"Hi {user_name}! Please give me a word: ")
wi_upcased = word_input.upper()
print(wi_upcased)