import copy

def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [list(d.strip()) for d in data]

def write_data(data,num):
	with open(f'output{num}.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def num_occupied_adjacent(data,I,J):
	c = 0
	if data[I][J]=='.':
		return 0

	for ii in [-1,0,1]:
		for jj in [-1,0,1]:
			if (ii==0 and jj==0) or I+ii<0 or I+ii>=len(data) or J+jj<0 or J+jj>=len(data[I]):
				continue
			else:
				if data[I+ii][J+jj] == '#':
					c = c+1
	return c


def num_occupied(data):
	return sum([d.count('#') for d in data])

def part1():
	data = read_data()
	
	num_changed = -1

	iteration = 1
	while num_changed!=0:
		num_changed=0
		
		tmp_data = copy.deepcopy(data)

		nums_all = []
		for ii in range(len(data)):
			nums = []
			for jj in range(len(data[ii])):
				q = data[ii][jj]
				n = num_occupied_adjacent(data, ii, jj)
				nums.append(n)
				if q =='L' and n==0:
					tmp_data[ii][jj] = '#'
					num_changed = num_changed+1
				elif q=='#' and n>=4:
					tmp_data[ii][jj] = 'L'
					num_changed = num_changed+1
			nums_all.append(nums)

		# print(nums_all)
		data = copy.deepcopy(tmp_data)
		write_data(data,iteration)
		iteration = iteration+1

	return num_occupied(data)


###


def find_vis_in_dir(data,I,J,ii,jj):
	for n in range(1,max(len(data),len(data[0]))):

		if (I+n*ii)<0 or (I+n*ii)>=len(data) or (J+n*jj)<0 or (J+n*jj)>=len(data[0]):
			return 0
		elif data[I+n*ii][J+n*jj] == 'L':
			return 0
		elif data[I+n*ii][J+n*jj] == '#':
			return 1


	return 0

def num_visible_vacant_seats(data, I, J):

	n = 0
	for ii in [-1,0,1]:
		for jj in [-1,0,1]:
			if ii==0 and jj==0:
				continue

			n = n+find_vis_in_dir(data,I,J,ii,jj)

	return n

def part2():
	data = read_data()
	
	num_changed = -1

	iteration = 1
	while num_changed!=0:
		num_changed=0
		
		tmp_data = copy.deepcopy(data)

		nums_all = []
		for ii in range(len(data)):
			nums = []
			for jj in range(len(data[ii])):
				q = data[ii][jj]
				n = num_visible_vacant_seats(data, ii, jj)
				nums.append(n)
				if q =='L' and n==0:
					tmp_data[ii][jj] = '#'
					num_changed = num_changed+1
				elif q=='#' and n>=5:
					tmp_data[ii][jj] = 'L'
					num_changed = num_changed+1
			nums_all.append(nums)

		# print(nums_all)
		data = copy.deepcopy(tmp_data)
		write_data(data,iteration)
		iteration = iteration+1

	return num_occupied(data)

# print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
