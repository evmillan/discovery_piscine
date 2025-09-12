#!/usr/bin/env python3
import sys

def array_of_names(names_dict):
    """
    Toma un diccionario con nombres como claves y apellidos como valores.
    Devuelve una lista con los nombres completos, con la primera letra de cada parte en mayúscula.
    
    Parámetros:
        names_dict (dict): Diccionario con nombres y apellidos.

    Retorna:
        list: Lista de nombres completos formateados correctamente.
    """
    full_names = []

    for first_name, last_name in names_dict.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)

    return full_names


# Ejemplo de uso (esto se puede comentar o eliminar si solo quieres el método)
if __name__ == "__main__":
    persons = {
        "juan": "perez",
        "maria": "lopez",
        "ana": "gomez",
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier",
        "emmanuel": "millan",
        "christopher": "arroyo"
    }

    nombres_completos = array_of_names(persons)
    print(nombres_completos)
