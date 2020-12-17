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

# a quick checker, because congruence solver requires relatively prime moduli
def are_relatively_prime(schedule):
	for s in schedule:
		for t in schedule:
			if s==t:
				continue 
			if np.gcd(s,t)!=1:
				return False
	return True

# because the numpy product returns a float, not an int
def prod(V):
	p = 1
	for v in V:
		p = p*v
	return p

# a linear congruence solver
# implemented using https://www.youtube.com/watch?v=zIFehsBHB8o&ab_channel=MathswithJay
def find_base_time(moduli, residues):
	import numpy as np

	Ss = moduli
	Bs = residues

	N = prod(Ss)
	Ns = [N//s for s in Ss]
	
	Xs = [pow(n,-1,s) for n,s in list(zip(Ns,Ss))]

	x = sum(b*n*x for b,n,x in zip(Bs,Ns,Xs))

	return x%N, N

# solves by 
def part2():

	data = read_data()
	toss = int(data[0])

	d = data[1].replace('x,',"np.nan,").replace('x','np.nan')
	schedule = eval(f'[{d}]')
	offsets = [int(ii) for ii in range(len(schedule)) if not np.isnan(schedule[ii])]
	schedule = [int(s) for s in schedule if not np.isnan(s)]


	# being cautious -- this method does not work is the schedules are not relatively prime
	if not are_relatively_prime(schedule):
		raise ValueError

	# finds the root time x, such that the later busses must be offset correctly
	# but the root time may not have the first bus arriving correctly,
	# so we loop and find the correct time for all busses subsequently.
	# this is because the linear congruence solver does not work 
	# if one of the congruences is ===0(mod b)

	# note that i am passing in -offsets, because the target time is given in a co-fashion
	x, N = find_base_time(schedule[1:], [-a for a in offsets[1:]])
	
	# increment by steps such that all busses but the first will arrive on time,
	# until the first bus is on time
	ii = 0
	while (x+N*ii)%schedule[0] != 0:
		ii = ii+1
	# i am sure there's a way to not loop that.  i don't care.

	return x+N*ii

print("part 1: {}".format(part1()))	
print("part 2: {}".format(part2()))
