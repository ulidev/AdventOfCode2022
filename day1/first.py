#Script for Advent of Code 2021 - Day1 problem 1
import os
import numpy as np


input = open('input.txt', 'r')

data = np.array(input.readlines())
data = np.where(data == '\n', -1, data).astype(int)

N = len(data)

counter = 0
max_found = 0
for i in range(N): 
	if data[i] != -1: counter += data[i]
	else: counter = 0
	max_found = max(max_found, counter)

print("Maximum calories found:", max_found)

