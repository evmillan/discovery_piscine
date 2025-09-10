#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    # print("No parameters were given.\n")
    print("none\n")
for i in range(1, len(sys.argv)):
    if type(sys.argv[i]) == str:
        # print(f"Parameter {i}: {sys.argv[i]}")
        print(f"{sys.argv[i]}")
        break
