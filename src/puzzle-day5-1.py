#!/usr/bin/env/python

max = 0
seats = []
with open('boarding_passes.txt','r') as file:
	for line in file:
		line = line.strip()
		row = reduce(lambda num, bit: ((num << 1) + bit), map(lambda _:1 if _ == 'B' else 0, line[:7]))
		seat = reduce(lambda num, bit: ((num << 1) + bit), map(lambda _:1 if _ == 'R' else 0, line[7::]))
		mul = (row * 8) + seat
		if (mul > max):
			max = mul
print(max)
