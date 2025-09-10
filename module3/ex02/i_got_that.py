#!/usr/bin/env python3
import os

user_name = os.getenv("USER")

answer_input = input(f"Hello {user_name}! What you gotta say? : ")
while answer_input != "STOP":
    answer_input = input("I got that! Anything else? : ")
    if answer_input == "STOP":
        break