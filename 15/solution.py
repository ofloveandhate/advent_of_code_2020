def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def part1():
	data = read_data()[0]
	data = eval(f'[{data}]')
	print(data)

	# import collections
	# times_spoken = collections.Counter()

	prev_time_spoken = {}
	for ii in range(len(data)-1):
		prev_time_spoken[data[ii]] = ii+1

	# for ii in range(len(data)-1):
	# 	times_spoken[data[ii]] = 1

	# print(times_spoken)
	# print(prev_time_spoken)
	seq = data[:-1]

	curr_num = data[-1]
	num_its = 30000000
	for ii in range(len(data),num_its+1):

		# print(f'\nturn {ii}')
		# print(f'previous times: {prev_time_spoken}')
		if curr_num in prev_time_spoken:
			# print(f'{curr_num} already spoken {ii} {prev_time_spoken[curr_num]}')
			next_num = ii-prev_time_spoken[curr_num]
		else:
			# print(f'{curr_num} never spoken')
			next_num = 0

		prev_time_spoken[curr_num] = ii
		seq.append(curr_num)
		curr_num = next_num

	# print(seq)
	# print(next_num)
	return seq[-1]
###



def part2():
	data = read_data()
	thing = []
	for a in thing:
		pass

	return

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
