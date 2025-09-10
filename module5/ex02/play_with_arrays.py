#!/usr/bin/env python3
import random

original_array = random.sample(range(-100, 100), 10)
new_array = []
for i in range(len(original_array)):
    if original_array[i] > 5:
        new_array.append(original_array[i] + 2)
print("Original array:", original_array)
print("New array:", new_array)