#!/usr/bin/env/python

yes_counts = 0
answers = []
with open('answers.txt','r') as file:
	for line in file:
		line = line.strip()
		if line == '':
			# calculate sum
			unique_answers = set(answers)	
			yes_counts += len(unique_answers)
			answers = []
		else:
			answers += line
print(yes_counts)
