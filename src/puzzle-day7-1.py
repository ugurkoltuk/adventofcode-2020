#!/usr/bin/env/python

import re
class Rule:
	def __init__(self, color):
		self.children = []
		self.color = color
	def add(self, child):
		self.children.append(child)

def canContain(parent, color):
	if color in parent.children:
		return True
	return False

def addRule(rule):
	if rule.color not in [_.color for _ in rules]:
		rules.append(rule)

rules = []
with open('baggage_rules.txt','r') as file:
	for line in file:
		line = line.strip()

		# First check for no other bags
		m = re.search('^([a-z ]+) bags contain no other bags.$', line)
		if (m is not None):
			addRule(Rule(m.group(1)))
			continue

		# skip the 'blabla bags contain' part
		m = re.search('^([a-z ]+) bags contain ', line)
		if (m is None):
			break

		rule = Rule(m.group(1))

		#chop the line's head off
		line = line[m.end():]

		# now find each rule and add to the parent
		while True:
			m = re.search('^\s*(\d+) ([a-z ]+) bags?(,|\.) ?', line)
			if (m is None):
				#no more rules left
				break
			for _ in xrange(0, int(m.group(1))):
				rule.add(m.group(2))
			line = line[m.end():]
		rules.append(rule)

new_container_found = True
#just to kick it off, we will remove this eventualy.
container_colors = ["shiny gold"]

while new_container_found:
	new_container_found = False
	for container_color in container_colors:
		for rule in rules:
			if canContain(rule, container_color) and rule.color not in container_colors:
				container_colors.append(rule.color)
				new_container_found = True

# -1 to ignore the initial shiny gold
print(len(container_colors) - 1)


