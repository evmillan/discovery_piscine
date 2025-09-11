#!/usr/bin/env python3
import sys

def upcase_it(text):
    return text.upper()

if __name__ == "__main__":
    sample = "hello"
    print(upcase_it(sample))


""" #!/usr/bin/env python3
import sys

def upcase_it(text):
    return text.upper()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sample = "hello"
        print("Debes introducir al menos un parametro \nEjemplo: ./upcase_it.py <texto>\n")
        sys.exit(f"Se imprime el texto por defecto: \n{upcase_it(sample)}")
    
    input_text = "\n".join(sys.argv[1:])  # Permite múltiples palabras
    print(upcase_it(input_text)) """
