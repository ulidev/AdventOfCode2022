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
for element in data:
	middle_point = int(len(element)/2)
	repeated = set(element[:middle_point]).intersection(element[middle_point:]).pop()
	points = getPoints(repeated)
	accumulated_counter += points

print("Points:", accumulated_counter)