#!/usr/bin/python3
import sys

# Verificar que se pasen exactamente 2 parámetros
if len(sys.argv) != 3:
    print("none\n")
else:
    min_range = int(sys.argv[1])  # Primer número: Comienzo del rango
    max_range = int(sys.argv[2])  # Segundo parámetro: Fin del rango
    if min_range >= max_range:
        print("none\n")
    else:
        array_generated = list(range(min_range, max_range + 1)) # El " + 1" es para incluir el número 'end'
        # Generar e imprimir la secuencia de números en el rango especificado
        """ print(", ".join(str(i) for i in range(min_range, max_range + 1)) + "\n")
        print(f"{', '.join(str(i) for i in range(min_range, max_range + 1))}\n")   
        print(f"{', '.join(map(str, range(min_range, max_range + 1)))}\n") """
        print(f"{array_generated}\n")