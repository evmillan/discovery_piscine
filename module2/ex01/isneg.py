#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
number_input = int(input(f"Hey, {user_name} what's your number? : "))

if number_input < 0:
    print("This number is negative.")
elif number_input > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")