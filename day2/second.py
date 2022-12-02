#Solution made by github.com/ulidev. Day 2 Problem 2

import os
import numpy as np

file = open("input.txt", 'r')
data = file.readlines()

N = len(data)

#A -> Opponent Rock 1
#B -> Opponent Paper 2
#C -> Opponent Scissor 3

#X -> Lose
#Y -> Draw
#Z -> Win


def getResult(round):
	op = round[0]
	my = round[2]
	base = 0
	if my == "Y":
		base = 3
		if op == "A" : return base + 1
		elif op == "B" : return base + 2
		return base + 3
	elif my == "Z":
		base = 6
		if op == "A" : return base + 2
		elif op == "B" : return base + 3
		return base + 1

	if op == "A" : return base + 3
	elif op == "B" : return base + 1
	return base + 2

getResultVectorized = np.vectorize(getResult)

result = getResultVectorized(data)

print("Sum result:", np.sum(result))
