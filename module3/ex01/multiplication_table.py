#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
number_input = int(input(f"Hi {user_name}! Please enter an integer number (1-9): "))

if number_input < 1 or number_input > 9:
    print(f"Error: Please {user_name} enter an integer number between 1 & 9")
else:
    index = number_input
    for index in range(0, 10):
        print(f"{index} x {number_input} = {index  * number_input}")