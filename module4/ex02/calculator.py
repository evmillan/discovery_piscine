#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
print(f"Hi {user_name}!")
input_number01 = int(input(f"Please, give me the first number: "))
input_number02 = int(input(f"Please, give me the second number: "))
print("Thank you!")
# operation = input(f"What operation would you like to perform? (+, -, * or /)\n")
print(f"{input_number01} + {input_number02} = {input_number01 + input_number02}")
print(f"{input_number01} - {input_number02} = {input_number01 - input_number02}")
print(f"{input_number01} * {input_number02} = {input_number01 * input_number02}")
print(f"{input_number01} / {input_number02} = {input_number01 / input_number02}")