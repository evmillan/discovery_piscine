#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
current_age = int(input(f"Hi {user_name}! Please tell me your age: "))
print(f"You are currently {current_age} years old.")
i = 1
for i in range(i, 4):
    print(f"In {i * 10} years, you'll be {current_age + i * 10} years old.")