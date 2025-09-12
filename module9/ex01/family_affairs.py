#!/usr/bin/env python3
import numpy as np

def np_find_the_redheads(family_dict):
    """
    Filtra los miembros de la familia con cabello rojo usando NumPy.

    Parámetros:
    family_dict (dict): Diccionario con nombres como claves y colores de cabello como valores.

    Retorna:
    list: Lista de nombres con cabello rojo, usando .tolist().
    """
    redheads = filter(lambda name: family_dict[name].lower() == 'red', family_dict.keys())
    return np.array(list(redheads)).tolist()

def find_the_redheads(family_dict):
    """
    Filtra los miembros de la familia con cabello rojo.

    Parámetros:
    family_dict (dict): Diccionario con nombres como claves y colores de cabello como valores.

    Retorna:
    list: Lista de nombres con cabello rojo.
    """
    redheads = filter(lambda name: family_dict[name].lower() == 'rojo', family_dict.keys())
    return list(redheads)


if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    family = {
        'Ana': 'rubio',
        'Luis': 'rojo',
        'Carla': 'castaño',
        'Pedro': 'rojo',
        'Elena': 'negro'
    }


    redheads = np_find_the_redheads(dupont_family)
    print(redheads)
    lochos = find_the_redheads(family)
    print(lochos)  # Output: ['Luis', 'Pedro']
