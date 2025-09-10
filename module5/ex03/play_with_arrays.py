#!/usr/bin/env python3
import random

# original_array = random.sample(range(-100, 100), 10)
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
seen = set()
aux_value = 0
for i in range(len(original_array)):
    if original_array[i] > 5:
        aux_value = original_array[i] + 2
        if aux_value not in seen:
            seen.add(aux_value)
            new_array.append(original_array[i] + 2)
set_array = set(new_array)
print("Original array:", original_array)
print("New array:", new_array)
# print("Set array:", set_array)
