#Solution made by github.com/ulidev. Day _ Problem _

import os
import numpy as np

def getPoints(target_char):
	if target_char >= 'A' and target_char <= 'Z':
		return ord(target_char) - ord('A') + 27
	return ord(target_char)- ord('a') + 1

file = open("input.txt", 'r')
data = np.array(file.readlines())

N = len(data)

accumulated_counter = 0
for i in range(0, N, 3):
	common = set(data[i]).intersection(data[i+1]).intersection(data[i+2])
	common.remove('\n')
	print(common)
	accumulated_counter += getPoints(common.pop())

print("Points:", accumulated_counter)

