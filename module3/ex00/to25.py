#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
number_input = int(input(f"Hi {user_name}! Please enter a number less than 25: "))

if number_input < 25:
    index = number_input
    while index <= 25:
        print(f"Inside the loop, my variable is {index}")
        index += 1
    else:
        print("Bucle terminado. A otra cosa mariposa!")
else:
    print(f"Overflow Error: ¡{user_name} el número ingresado debe ser menor a 25!")