def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###
import numpy as np

def part1():
	data = read_data()
	objective = int(data[0])
	d = data[1].replace('x,',"").replace('x','')
	schedule = eval(f'[{d}]')
	schedule = [int(s) for s in schedule]

	times = [s*(objective//s+1) for s in schedule]
	m = min(times)
	i = np.argmin(times)
	diff = m-objective
	
	return diff*schedule[i]


###

def condition_satisfied(times, offsets):
	assert(len(times)==len(offsets))
	# 
	for ii in range(len(times)):
		d = times[ii]-times[0]

		if d!=offsets[ii]:
			return False
	print(times, offsets, [t-times[0] for t in times])
	return True






def part2():
	data = read_data()
	toss = int(data[0])

	d = data[1].replace('x,',"np.nan,").replace('x','np.nan')
	schedule = eval(f'[{d}]')
	offsets = [ii for ii in range(len(schedule)) if not np.isnan(schedule[ii])]
	schedule = [s for s in schedule if not np.isnan(s)]

	as_one = list(zip(schedule, offsets))


	as_one.sort()

	# factor = 2
	factor = 100000000000000//min(schedule)-1
	while True:
		

		threshold = factor*min(schedule)

		# if factor%1000==0:
		# 	print(factor, threshold)

		times = [s*(threshold//s+1) for s in schedule]
		timestamp = min(times)
		if condition_satisfied(times, offsets):
			return timestamp

		factor = factor+1

# print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
