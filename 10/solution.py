def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	data = [int(d.strip()) for d in data]
	data.sort()
	return data

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###



def part1():

	data = read_data()
	from collections import defaultdict
	diffs = defaultdict(int)
	diffs[1] = 1
	diffs[3] = 1
	for ii in range(len(data)-1):
		diff = data[ii+1]-data[ii]
		diffs[diff] = diffs[diff]+1

	return diffs[3]*diffs[1]


###

def num_candidates(data, ind):
	n = 0
	for ii in range(1,4):
		# if out of range or out of val
		if (ind+ii)<len(data) and (data[ind+ii]-data[ind])<=3:
			n = n+1
	return n


def ind_next_non_one(data, ind):
	ii = 1
	while num_candidates(data,ind+ii)==1:
		ii = ii+1

	return ind+ii

def ind_next_one(data, ind):
	ii = 1
	while num_candidates(data,ind+ii)!=1:
		ii = ii+1

	return ind+ii

def possibilites(data, ind):

	s = 0
	for ii in range(1,num_candidates(data, ind)):
		s = s + possibilites(data,ind+ii)

	return s


def process_block(data, ind):
	nums = []
	for ii in range(1,1+num_candidates(data, ind)):
		n = num_candidates(data, ind+ii)
		if n==1:
			nums.append(1)
		else:
			nums.append(process_block(data,ind+ii))


	import numpy as np
	n = np.sum(nums)

	return n

def part2():
	data = read_data()
	# write_data(data)
	p = 1

	data = [0]+data+[max(data)+3] # take care of boundary conditions

	if num_candidates(data,0)==1:
		ii = ind_next_non_one(data,0)
	else:
		ii=0

	block_numbers = []
	while ii<len(data)-1:
		block_numbers.append(process_block(data, ii))

		#skip to next block
		ii = ind_next_one(data, ii)
		ii = ind_next_non_one(data, ii)

	import numpy as np
	return np.prod(block_numbers)

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
