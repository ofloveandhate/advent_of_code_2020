def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [int(d.strip()) for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def possibilities(data, index, num):
	poss = set()
	for d in data[index: index+num]:
		for e in data[index+1: index+num]:
			if d != e:
				poss.add(d+e)
	return poss

def part1():

	num = 25

	data = read_data()

	for ii in range(num, len(data)):
		d = data[ii]
		if d not in possibilities(data, ii-num, num):
			return d


###



def part2():
	p1 = part1()
	data = read_data()

	for span in range(2,len(data)-1):
		for ii in range(len(data)-span):
			q = data[ii:ii+span]
			if sum(q) == p1:
				print(p1, min(q), max(q))
				return min(q)+max(q)


print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
