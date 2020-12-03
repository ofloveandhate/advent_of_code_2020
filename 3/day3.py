
def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return data


def part1():
	data = read_data()

	counter = 0
	y = 0

	for ii in range(1,len(data)):
		d = data[ii].strip()
		y = (y+3)%len(d)
		is_tree = d[y] == '#'

		if is_tree:
			counter = counter+1

	return counter

def count(y_s, x_s, data):

	x = 0
	y = 0
	counter = 0

	x = x+x_s
	while x < len(data):
		d = data[x].strip()
		y = (y+y_s)%len(d)
		is_tree = d[y] == '#'
		

		if is_tree:
			counter = counter+1

		x = x+x_s
	return counter

def part2():
	data = read_data()


	slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

	# slopes = [(1,1),(3,1)]
	prod = 1
	for s in slopes:
		
		c = count(s[0],s[1],data)
		print(c)
		prod = prod*c


	return prod

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))