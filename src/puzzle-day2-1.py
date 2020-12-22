#!/usr/bin/env/python

import re

valid_passwords=0
with open('passwords.txt','r') as file:
	for line in file:
		match = re.search("(\d+)-(\d+) ([a-z]): (.*)", line)
		min_ocr = int(match.group(1))
		max_ocr = int(match.group(2))
		letter = match.group(3)
		password = match.group(4)
		if (password.count(letter) >= min_ocr and password.count(letter) <= max_ocr):
			valid_passwords = valid_passwords + 1

print(valid_passwords)
