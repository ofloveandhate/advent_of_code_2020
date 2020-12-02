def part1():
	with open ('input.txt') as f:
		nums = [int(ell) for ell in f.readlines()]

	print(nums)

	s = 2020
	for n in nums:
		for m in nums:
			if n+m==s:
				print(n*m)

def part2():
	with open ('input.txt') as f:
		nums = [int(ell) for ell in f.readlines()]

	print(nums)

	s = 2020
	for n in nums:
		for m in nums:
			for k in nums:
				if n+m+k==s:
					print(n*m*k)
					return

part2()

			