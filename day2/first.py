#Solution made by github.com/ulidev. Day 2 Problem 1

import os
import numpy as np

file = open("input.txt", 'r')
data = file.readlines()

N = len(data)

#A -> Opponent Rock
#B -> Opponent Paper
#C -> Opponent Scissor

#X -> My Rock
#Y -> My Paper
#Z -> My Scissor


def getResult(round):
	op = round[0]
	my = round[2]
	counter = 1
	if my == "Y":
		counter += 1
	elif my == "Z":
		counter += 2

	if (my == "X" and op == "C") or (my == "Y" and op == "A") or (my == "Z" and op == "B"):
		return (counter + 6)
	if (my == "X" and op == "A") or (my == "Y" and op == "B") or (my == "Z" and op == "C"):
		return counter + 3
	return counter

getResultVectorized = np.vectorize(getResult)

result = getResultVectorized(data)

print("Sum result:", np.sum(result))
