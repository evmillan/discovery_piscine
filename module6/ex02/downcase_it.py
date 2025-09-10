#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    # print("No parameters were given.\n")
    print("none\n")
else:
    lower_parameter = sys.argv[1].lower()
    print(f"{lower_parameter} \n")