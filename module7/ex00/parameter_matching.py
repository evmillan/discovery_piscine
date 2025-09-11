#!/usr/bin/python3
import sys
import os

user_name = os.getenv('USER')

# Verificar que se pase exactamente 1 parámetro
if len(sys.argv) != 2:
    print("none\n")
else:
    print(f"Hello {user_name}, welcome to the program!\n")
    input_str = input(f"What was the parameter? ")
    input_param = sys.argv[1]
    # Comparar la entrada del usuario con el parámetro pasado al script
    if input_str == input_param:
        print("Good job!\n")
    else:
        print("Nope, sorry...\n")