#!/usr/bin/env python3
import sys

def downcase_it(text):
    return text.lower()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sample = "none"
        print("Debes introducir al menos un parametro \nEjemplo: ./upcase_it.py <texto>\n")
        sys.exit(f"Se imprime el texto por defecto: \n{downcase_it(sample)}")
    
    input_text = "\n".join(sys.argv[1:])  # Permite múltiples palabras
    print(downcase_it(input_text))