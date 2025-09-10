#!/usr/bin/python3
import sys

# Verificar si hay al menos dos parámetros
if len(sys.argv) > 2:
    # Imprimir los parámetros en orden invertido
    for param in reversed(sys.argv[1:]): #sys.argv[::-1]: 
        print(f"{param}")
else:
    print("none\n")
