#Script for Advent of Code 2021 - Day1 problem 2
import os
import numpy as np


input = open('input.txt', 'r')
data = np.array(input.readlines())
data = np.where(data == '\n', -1, data).astype(int)

N = len(data)

top = np.full((3), 0)
counter = 0
max_found = 0
for i in range(N): 
	if data[i] != -1: counter += data[i]
	else:
		top = np.append(top, counter)
		top = np.sort(top)
		top = np.flip(top)[0:3]
		counter = 0


print("The top three values are:",top)
print("The sum of which is", np.sum(top))

