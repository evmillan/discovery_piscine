#!/usr/bin/env python3
import os
i = 0
while i <= 10:
    print(f"Table of {i}:", end="")
    j = 0
    while j <= 10:
        print(f" {i * j}", end="")
        j += 1
    i += 1
    print()