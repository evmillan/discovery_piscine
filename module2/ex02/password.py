#!/usr/bin/env python3
import os

user_name = os.getenv("USER")
password = "Python is awesome"
pasword_input = input(f"Hey, {user_name} what's your password? : ")

if pasword_input == password:
  print("ACCESS GRANTED")
else:
  print("ACCESS DENIED")