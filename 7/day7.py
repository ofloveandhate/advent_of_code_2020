def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [clean_text(d.strip()) for d in data if d]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

def clean_text(d):
	return d.replace('bags contain',':').replace('bags,','!').replace('bag,','!').replace('bags.','').replace('bag.','')
###



def make_map_entry(d):
	# print(d)
	outer,b = d.split(':')

	inner = {}
	if 'no other' not in b:
		c1 = [q.strip() for q in b.split('!')]
		for c in c1:
			num = int(c.split()[0])
			inner[c.split()[1]+" "+c.split()[2]] = num

	return (outer.strip(), inner)

def make_bagmap():
	data = read_data()

	bagmap = {}
	for ii in range(len(data)):
		d = data[ii]
		a,b = make_map_entry(d)
		bagmap[a] = b
	return bagmap


def can_directly_contain(m, k, v):
	if v in m[k]:
		return True
	else:
		return False


def part1():
	bagmap = make_bagmap()

	yep = set()

	find_me = ['shiny gold']
	found_me = []
	while len(find_me)>0:

		for f in find_me:

			for k in bagmap.keys():

				if can_directly_contain(bagmap, k, f):

					found_me.append(k)
					yep.add(k)

		find_me = found_me.copy()
		found_me = []

	return len(yep)


###

def nested_count(m,k):
	count = 1
	for color, c in m[k].items():
		count = count+c*nested_count(m,color)

	return count

def part2():
	bagmap = make_bagmap()
	find_me = 'shiny gold'

	return nested_count(bagmap,find_me)-1 
	# off by 1, because we're not counting the top bag -- just those it contains.
		


print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
