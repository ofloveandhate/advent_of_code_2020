import numpy as np

s = 2020

def read_data():
	with open ('input.txt') as f:
		nums = np.array([int(ell) for ell in f.readlines()])
	return nums

def part1():
	nums = read_data()

	s = 2020
	for n in nums:
		for m in nums:
			if n+m==s:
				print(n*m)
				return

def part2():
	nums = read_data()

	for n in nums:
		for m in nums:
			for k in nums:
				if n+m+k==s:
					print(n*m*k)
					return

part2()

			