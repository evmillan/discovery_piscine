#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
# input_str = "Hey, " + user_name + " what's your number? : "
# number_input = int(input(input_str))
number_input = int(input(f"Hey, {user_name} what's your number? : "))

if number_input == 0:
    print("This number is equal to zero.")
else:
    print("This number is different from zero.")