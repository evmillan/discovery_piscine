#!/usr/bin/python3
import sys

# Verificar que se pasen exactamente 2 parámetros
if len(sys.argv) != 2:
    print("none\n")
else:
    search_str = "z"  # Cadena a buscar
    target_str = sys.argv[1]  # Parámetro: string donde buscar
    
    # Contar las ocurrencias del primer parámetro en el segundo
    count = target_str.count(search_str)
    
    # Si el conteo es mayor que 0, mostrar el número de ocurrencias, si no, mostrar "none"
    if count > 0:
        print(f"There are {count} ocurrences of the string {search_str}")
        for i in target_str:
            if i == search_str:
                print(i, end="")
    else:
        print("none\n")