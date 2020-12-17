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




def initialize_state(num_cycles):
	data = read_data()

	num_x = len(data[0]) + 2*num_cycles
	num_y = len(data) + 2*num_cycles
	num_z = 1+2*num_cycles

	state_curr = np.zeros( (num_z, num_x, num_y) )

	for ii in range(len(data)):
		d = data[ii]
		for jj in range(len(d)):
			q = d[jj]

			state_curr[num_cycles,num_cycles+ii,num_cycles+jj] = 1 if q=='#' else 0

	return state_curr


def num_active_neighbors(x,y,z, state):
	nx, ny, nz = state.shape

	a = max(0,x-1),min(nx+1,x+2)
	b = max(0,y-1),min(ny+1,y+2)
	c = max(0,z-1),min(nz+1,z+2)

	core = state[a[0]:a[1], b[0]:b[1], c[0]:c[1]]

	num_core = threesome(state[a[0]:a[1], b[0]:b[1], c[0]:c[1]]) - state[x,y,z]
	# only subtract 1 if the location is ON.
	return num_core

def threesome(arr):
	return sum(sum(sum(arr)))


def simulate_step(state_curr):
	state_next = np.zeros_like(state_curr)

	size = state_curr.shape

	for ii in range(size[0]):
		# print(f'layer {ii}')
		for jj in range(size[1]):
			for kk in range(size[2]):

				n = num_active_neighbors(ii,jj,kk, state_curr)
				if state_curr[ii,jj,kk]:
					# print(f'[{ii},{jj},{kk}] active, {n} active neighbors')
					state_next[ii,jj,kk] = 1 if (n==2 or n==3) else 0
				else:
					# print(f'[{ii},{jj},{kk}] inactive, {n} active neighbors')
					state_next[ii,jj,kk] = 1 if n==3 else 0

	return state_next


def part1():
	num_cycles = 6
	state_curr = initialize_state(num_cycles)
	

	for c in range(num_cycles):
		# print(f'\ncycle {c}')
		state_next = simulate_step(state_curr)
		state_curr = state_next
		# print(state_curr)


	return threesome(state_curr)


###



def part2():
	data = read_data()
	thing = []
	for a in thing:
		pass

	return

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
