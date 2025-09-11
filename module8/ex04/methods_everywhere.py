#!/usr/bin/env python3

import sys

# Método shrink
def shrink(text):
    # Mostrar los primeros ocho caracteres
    print(text[:8])

# Método enlarge
def enlarge(text):
    # Añadir 'Z' hasta que la longitud sea 8
    # result = text.ljust(8, 'Z')
    # print(result)
    while len(text) < 8:
        text += 'Z'
    print(text)

def main():
    # Iteramos sobre los argumentos pasados al programa
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)  # Si tiene exactamente 8 caracteres, se imprime tal cual

if __name__ == "__main__":
    main()
