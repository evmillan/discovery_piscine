#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    # print("No parameters were given.\n")
    print("none\n")
else:
    upper_parameter = sys.argv[1].upper()
    print(f"{upper_parameter} \n")