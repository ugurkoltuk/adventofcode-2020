#!/usr/bin/env/python

from collections import Counter
yes_counts = 0
c = Counter()
population = 0
with open('answers.txt','r') as file:
	for line in file:
		line = line.strip()
		if line == '':
			yes_counts += len(filter(lambda _: True if _[1] == population else False, c.items()))
			population = 0
			c = Counter()
		
		else:
			c += Counter(line)
			population += 1
print(yes_counts)
