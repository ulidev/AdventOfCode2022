#Solution made by github.com/ulidev. Day _ Problem _

import os
import numpy as np

file = open("input.txt", 'r')
data = file.readlines()

N = len(data)

accumulated_counter = 0
for element in data:
	first, second = element.split(",")
	first_start, first_end = first.split("-")
	second_start, second_end = second.split("-")
	first_start = int(first_start)
	first_end = int(first_end)
	second_start = int(second_start)
	second_end = int(second_end)
	if (second_start > first_end or first_start > second_end): accumulated_counter += 1

print("Partially or fully overlapped:", N-accumulated_counter)
