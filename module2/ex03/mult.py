#!/usr/bin/env python3
import os

user_name = os.getenv("USER")

print(f"Hi {user_name}!")
input_number01 = int(input(f"Please enter the first number:\n"))
input_number02 = int(input(f"Please enter the second number:\n"))
mult_result = input_number01 * input_number02

if mult_result > 0:
    print(f"{input_number01} x {input_number02} = {mult_result}")
    print("The result is positive.")
elif mult_result < 0:
    print(f"{input_number01} x {input_number02} = {mult_result}")
    print("The result is negative.")
else:
    print(f"{input_number01} x {input_number02} = {mult_result}")
    print("The result is positive and negative.")