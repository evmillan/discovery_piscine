#!/usr/bin/env python3

import sys

# Definimos el método add_one que recibe un parámetro y le agrega 1
def add_one(num):
    return num + 1

def main():
    # Inicializamos la variable
    my_var = 5
    
    # Mostramos la variable antes de llamarla
    print(f"Antes de add_one: {my_var}")
    
    # Llamamos al método add_one
    my_var = add_one(my_var)
    
    # Mostramos la variable después de la llamada
    print(f"Después de add_one: {my_var}")

if __name__ == "__main__":
    main()