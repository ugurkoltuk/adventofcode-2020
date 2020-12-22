#!/usr/bin/env/python

import re

passport_complete = False

passport = {}

required_fields = [
"byr",
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid"]

def is_valid(passport):
	for required_field in required_fields:
		if required_field not in passport:
			print("Invalid passport because it is missing " + str(required_field))
			return False
	return True
valid_passports = 0
with open('batch.txt','r') as file:
	for line in file:
		passport_complete = (line.strip() == '')
		if passport_complete:
			if is_valid(passport):
				valid_passports = valid_passports + 1
				print("THIS IS A VALID PASSPORT")
			print(passport) 
			passport = {}
		else:
			fields = re.split("\s+", line.strip())
			for field in fields:
				kvp = re.split(":", field.strip())
				passport[kvp[0].strip()] = kvp[1].strip()
print(valid_passports)
