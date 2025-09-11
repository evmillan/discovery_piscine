#!/usr/bin/env python3
import sys

counter = 0
if len(sys.argv) < 2:
    # print("No parameters were given.\n")
    print("none\n")
else:
    
    for arg in sys.argv[1:]: #range(1, len(sys.argv)):
        # Si el argumento no termina con "ism", lo mostramos con "ism" añadido
        if arg.find("ism") != len(arg) - 3: #rfind previene errores si ism está en medio
        # if not arg.endswith("ism"):
            print(arg + "ism")
            counter += 1
print(f"{counter} sufix appended of {len(sys.argv) - 1} total parameters")