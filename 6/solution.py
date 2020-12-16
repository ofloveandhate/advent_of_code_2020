def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def make_groups1():
	data = read_data()
	groups = []
	g = ''
	for d in data:
		if len(d):
			g = g+d

		else:
			groups.append(g)
			g = ''
	return groups

def part1():
	groups = make_groups1()

	c = 0
	for g in groups:
		q = set(g)
		c = c+ len(q)
	return c

###


def make_groups2():
	data = read_data()
	groups = []
	g = ''
	c = 0
	for d in data:
		if len(d):
			g = g+d
			c = c+1
		else:
			groups.append((g,c))
			g = ''
			c = 0
	return groups


def part2():
	groups = make_groups2()

	c = 0
	for g in groups:
		import collections
		q = collections.Counter(g[0])
		print(q)
		print(g[1])
		for a,b in q.items():
			if b==g[1]:
				c = c+1
	return c

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
