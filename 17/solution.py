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




def initialize_state(num_cycles, dimension):
	data = read_data()

	num_x = len(data[0]) + 2*num_cycles
	num_y = len(data) + 2*num_cycles
	num_z = 1+2*num_cycles
	num_w = 1 if dimension==3 else 1+2*num_cycles

	state_curr = np.zeros( (num_w, num_z, num_x, num_y) )

	w_ind = 0 if dimension==3 else num_cycles

	for ii in range(len(data)):
		d = data[ii]
		for jj in range(len(d)):
			q = d[jj]

			state_curr[w_ind, num_cycles,num_cycles+ii,num_cycles+jj] = 1 if q=='#' else 0

	return state_curr


def num_active_neighbors(w,x,y,z, state):
	nw, nx, ny, nz = state.shape

	q = max(0,w-1),min(nw+1,w+2)
	a = max(0,x-1),min(nx+1,x+2)
	b = max(0,y-1),min(ny+1,y+2)
	c = max(0,z-1),min(nz+1,z+2)

	core = state[q[0]:q[1],a[0]:a[1], b[0]:b[1], c[0]:c[1]]

	num_core = foursome(core) - state[w,x,y,z]
	# only subtract 1 if the location is ON.
	return num_core

def foursome(arr):
	return sum(sum(sum(sum(arr))))


def simulate_step(state_curr):
	state_next = np.zeros_like(state_curr)

	size = state_curr.shape

	for ii in range(size[0]):
		for jj in range(size[1]):
			for kk in range(size[2]):
				for ll in range(size[3]):
					n = num_active_neighbors(ii,jj,kk,ll, state_curr)
					state_curr[ii,jj,kk,ll]
					if state_curr[ii,jj,kk,ll]:
						state_next[ii,jj,kk,ll] = 1 if (n==2 or n==3) else 0
					else:
						state_next[ii,jj,kk,ll] = 1 if n==3 else 0

	return state_next


def part1():
	num_cycles = 6
	state_curr = initialize_state(num_cycles, 3)
	

	for c in range(num_cycles):
		state_next = simulate_step(state_curr)
		state_curr = state_next


	return foursome(state_curr)


###



def part2():
	num_cycles = 6
	state_curr = initialize_state(num_cycles, 4)
	

	for c in range(num_cycles):
		state_next = simulate_step(state_curr)
		state_curr = state_next


	return foursome(state_curr)

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
