def read_data():
	with open ('input.txt') as f:
		data = f.readlines()

	data = [d.strip() for d in data]
	return [(d[0],int(d[1:])) for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

import numpy as np
C = np.complex
i = C(0,1)
def do_it(action, num, direction):

	if action=='E':
		return num*C(1,0), direction

	elif action=='N':
		return num*C(0,1), direction

	elif action=='S':
		return num*C(0,-1), direction

	elif action=='W':
		return num*C(-1,0), direction

	elif action=='F':
		return num*direction, direction

	elif action=='R':
		return 0, direction*i**(-num/90)
	elif action=='L':
		return 0, direction*i**(num/90)



def part1():
	data = read_data()

	position = C(0,0)
	direction = C(1,0)
	for ii in range(len(data)):
		action, num = data[ii]

		delta, direction = do_it(action, num, direction)
		position = position + delta

	print(position)
	return abs(position.real) + abs(position.imag)


###



def part2():
	data = read_data()

	position = C(0,0)
	waypoint = C(10,1)
	direction = C(1,0)
	for ii in range(len(data)):
		action, num = data[ii]

		if action=='E':
			waypoint = waypoint + num*C(1,0)

		elif action=='N':
			waypoint = waypoint + num*C(0,1)

		elif action=='S':
			waypoint = waypoint + num*C(0,-1)

		elif action=='W':
			waypoint = waypoint + num*C(-1,0)

		elif action=='F':
			position = position + num*waypoint

		elif action=='R':
			waypoint = waypoint*i**(-num/90)
		elif action=='L':
			waypoint = waypoint*i**(num/90)


	print(position)
	return abs(position.real) + abs(position.imag)

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
