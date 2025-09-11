#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    # print("No parameters were given.\n")
    print("none\n")
else:
    print("Number of parameters:", len(sys.argv) - 1)
    for i in range(1, len(sys.argv)):
        print(f"Parameter {i} = {sys.argv[i]}: {len(sys.argv[i])} characters")