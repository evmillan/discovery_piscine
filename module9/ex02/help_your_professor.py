#!/usr/bin/env python3

# Método para calcular el promedio de la clase
def average(grades_dict):
    # Verificar que el diccionario no esté vacío
    if len(grades_dict) == 0:
        return 0  # Si no hay estudiantes (diccionario vacío), el promedio es 0
    
    # Calcular la suma total de las puntuaciones
    total_score = sum(grades_dict.values())
    
    # Calcular el número de estudiantes
    num_students = len(grades_dict)
    
    # Calcular el promedio
    class_average = total_score / num_students
    
    return class_average


# Ejemplo de uso del método 'average'
if __name__ == "__main__":
    # Diccionario con los nombres de los estudiantes y sus puntuaciones
    class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
    }
    class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
    }
    
    # Llamada al método 'average' y mostrar el resultado
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
