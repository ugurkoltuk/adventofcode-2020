#!/usr/bin/env/python

import re

passport_complete = False

passport = {}

def byr_validator(byr):
	return int(byr) >= 1920 and int(byr) <= 2002

def iyr_validator(iyr):
	return int(iyr) >= 2010 and int(iyr) <= 2020

def eyr_validator(eyr):
	return int(eyr) >= 2020 and int(eyr) <= 2030

def hgt_validator(hgt):
	m = re.match('(\d+)(cm|in)', hgt)
	if (m is None):
		return False
	len = m.group(1)
	unit = m.group(2)
	if (unit == 'cm'):
		if (int(len) < 150 or int(len) > 193):
			return False
	if (unit == 'in'):
		if (int(len) < 59 or int(len) > 76):
			return False
	if (unit != 'in' and unit != 'cm'):
		return False
	return True

def hcl_validator(hcl):
	return  re.match('#[0-9a-f]{6}', hcl) is not None

def ecl_validator(ecl):
	return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] 

def pid_validator(pid):
	return re.match('^[0-9]{9}$', pid) is not None

required_fields = {
	"byr": byr_validator,
	"iyr": iyr_validator,
	"eyr": eyr_validator,
	"hgt": hgt_validator,
	"hcl": hcl_validator,
	"ecl": ecl_validator,
	"pid": pid_validator,
}

def is_valid(passport):
	for required_field, validator in required_fields.items():
		if required_field not in passport:
			return False
		if not validator(passport[required_field]):
			return False
	return True
valid_passports = 0
with open('batch.txt','r') as file:
	for line in file:
		passport_complete = (line.strip() == '')
		if passport_complete:
			if is_valid(passport):
				valid_passports = valid_passports + 1
			passport = {}
		else:
			fields = re.split("\s+", line.strip())
			for field in fields:
				kvp = re.split(":", field.strip())
				passport[kvp[0].strip()] = kvp[1].strip()
print(valid_passports)
