def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def row(txt):

	txt = txt.replace('F','0')
	txt = txt.replace('B','1')
	a = int(txt,2)

	return a

def col(txt):

	txt = txt.replace('L','0')
	txt = txt.replace('R','1')
	a = int(txt,2)

	return a

def p1(txt):
	return row(txt[:7]), col(txt[7:])

def seat_id(r,c):
	return r*8 + c

def part1ids():
	data = read_data()
	ids = []
	for ii in range(len(data)):
		print(data[ii])
		r,c = p1(data[ii])
		ids.append(seat_id(r,c))
	return ids

def part1():
	return max(part1ids())
###



def part2():

	all_seats = set(range(part1()))
	present_seats = set(part1ids())

	print(all_seats - present_seats)
	return

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
