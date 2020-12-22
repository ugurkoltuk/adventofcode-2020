#!/usr/bin/env/python

import re

trees=0
pos=0

with open('forest.txt','r') as file:
	for line in file:
		if (line[pos] == '#'):
			trees = trees + 1 
		pos = (pos + 3) % (len(line) - 1)
print(trees)
