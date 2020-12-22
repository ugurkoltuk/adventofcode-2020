#!/usr/bin/env/python

import re

mul=1
slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

for slope in slopes:
	trees = 0
	pos = 0
	row = -1
	with open('forest.txt','r') as file:
		for line in file:
			row = row + 1
			if (row % slope[0] != 0):
				continue
			if (line[pos] == '#'):
				trees = trees + 1 
			pos = (pos + slope[1]) % (len(line) - 1)
	print(trees)
	mul = mul * trees
print(mul)
