#!/usr/bin/env python3
import os
import math

user_name = os.getenv("USER")
print(f"Hi {user_name}!")
input_number = float(input(f"Please, give me a number: "))
rounded_number = math.ceil(input_number)
print(f"The rounded up value of {input_number} is:\n {rounded_number}")