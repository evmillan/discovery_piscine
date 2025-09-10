#!/usr/bin/env python3
import os
import math

user_nme = os.getenv("USER")
print(f"Hi {user_nme}!")
input_number = float(input(f"Please, give me a number: "))
f, i = math.modf(input_number)

if f == 0:
    print(f"The number {input_number} is an integer.")
else:
    print(f"The number {input_number} is a decimal.")