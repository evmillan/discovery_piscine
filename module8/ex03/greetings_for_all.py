#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Welcome, {name}!")
    else:
        print("Error: The name must be a string.")

# Ejemplo de uso:
if __name__ == "__main__":
    greetings()               # Llama sin argumento → usa valor por defecto
    greetings("Emmanuel")        # Llama con string
    greetings(1234)            # Llama con tipo incorrecto
    greetings(["Millan"])        # Llama con tipo incorrecto

if __name__ == "__main__":
    user_input = input("Please enter your name (or press Enter to remain a 'noble stranger'): ")

    # Si el usuario no escribe nada, usamos el valor por defecto
    if user_input.strip() == "":
        greetings()
    else:
        greetings(user_input)
