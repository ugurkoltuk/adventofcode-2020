#!/usr/bin/env/python

import re
class Rule:
	def __init__(self, color):
		self.children = []
		self.color = color
	def add(self, child):
		self.children.append(child)
	def totalChildrenCount(self):
		result = len(self.children)
		for child in self.children:
			result += findRule(child).totalChildrenCount()
		return result

def findRule(color):
	r = filter(lambda _: _.color == color, rules)
	if len(r) != 1:
		print("Something went wrong, for %s there are %d rules" % (color, len(r)))
	return r[0]

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

print(findRule('shiny gold').totalChildrenCount())

