#!/usr/bin/python3
import sys

# Verificar que se pasen exactamente 2 parámetros
if len(sys.argv) != 3:
    print("none\n")
else:
    search_str = sys.argv[1]  # Primer parámetro: cadena para buscar
    target_str = sys.argv[2]  # Segundo parámetro: string donde buscar
    
    # Contar las ocurrencias del primer parámetro en el segundo
    count = target_str.count(search_str)
    
    # Si el conteo es mayor que 0, mostrar el número de ocurrencias, si no, mostrar "none"
    if count > 0:
        print(f"{count}\n")
    else:
        print("none\n")
