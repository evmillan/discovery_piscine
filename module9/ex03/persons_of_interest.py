#!/usr/bin/env python3

# Método para ordenar y mostrar las figuras históricas por año de nacimiento
def famous_births(persons):
    # Ordenamos el diccionario por el año de nacimiento
    sorted_persons = sorted(persons.items(), key=lambda x: x[1]['year_of_birth'])
    
    # Mostrar cada entrada (nombre y año de nacimiento)
    for person in sorted_persons:
        name = person[1]['name']
        year_of_birth = person[1]['year_of_birth']
        print(f"{name} is a great scientist born in {year_of_birth}")


# Ejemplo de uso del método 'famous_births'
if __name__ == "__main__":
    # Diccionario de figuras históricas con nombre y año de nacimiento
    historical_figures = {
        "Einstein": {"name": "Albert Einstein", "year_of_birth": 1879},
        "Newton": {"name": "Isaac Newton", "year_of_birth": 1642},
        "Curie": {"name": "Marie Curie", "year_of_birth": 1867},
        "Darwin": {"name": "Charles Darwin", "year_of_birth": 1809},
        "Galileo": {"name": "Galileo Galilei", "year_of_birth": 1564}
    }
    women_scientists = {
    "ada": { "name": "Ada Lovelace", "year_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "year_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "year_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "year_of_birth": "1906" }
    }
    
    # Llamada al método 'famous_births' para ordenar y mostrar las figuras históricas y mujeres científicas
    famous_births(historical_figures)
    famous_births(women_scientists)
    # print(chr(sum(range(ord(min(str(not())))))))