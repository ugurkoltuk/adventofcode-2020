#!/usr/bin/env/python

seats = []
with open('boarding_passes.txt','r') as file:
	for line in file:
		line = line.strip()
		row = reduce(lambda num, bit: ((num << 1) + bit), map(lambda _:1 if _ == 'B' else 0, line[:7]))
		seat = reduce(lambda num, bit: ((num << 1) + bit), map(lambda _:1 if _ == 'R' else 0, line[7::]))
		mul = (row * 8) + seat
		seats.append(mul)

seats.sort()
prevseat = seats[0]
for seat in seats[1:]:
	if seat - prevseat > 1:
		if (prevseat + 1 != seat - 1):
			print("ok what")
		else:
			print(prevseat + 1)
		break
	prevseat = seat

