#!/usr/bin/env/python

import re

valid_passwords=0
with open('passwords.txt','r') as file:
	for line in file:
		match = re.search("(\d+)-(\d+) ([a-z]): (.*)", line)
		first_idx= int(match.group(1))
		second_idx = int(match.group(2))
		letter = match.group(3)
		password = match.group(4)
		if ((password[first_idx-1] == letter) != (password[second_idx-1] == letter)):
			valid_passwords = valid_passwords + 1

print(valid_passwords)
