def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')






# the magic function that makes it all work.  
# wow, it took forever to get this right.
def recursive_construct(L):

	poss = []

	if len(L)==1:
		for ell in L:
			poss.extend(ell)
	elif len(L)==2:
		for ell in L[0]:
			for emm in L[1]:
				poss.append(ell+emm)
	else:
		for ell in L[0]:
			for emm in recursive_construct(L[1:]):
				poss.append(ell+emm)
	return poss



class Seq(object):
	"""docstring for Seq"""
	def __init__(self, text):
		super(Seq, self).__init__()

		# print(f'making Seq from {text}')
		to_list = lambda x: [int(t) for t in x.split()]


		self.sequence = to_list(text)

	def __str__(self):
		return f'Seq: {self.sequence}'
	def __repr__(self):
		return str(self)

	def construct(self, graph):
		poss = [graph[t].construct(graph) for t in self.sequence]

		return recursive_construct(poss)



class Option(object):
	"""docstring for Rule"""
	def __init__(self, text):
		super(Option, self).__init__()
		# print(f'making Option from {text}')

		self.options =  [Seq(t) for t in text.split('|')]

	def __str__(self):
		return f'Option: {self.options}'
	def __repr__(self):
		return str(self)


	# always returns a list
	def construct(self, graph):
		opts = [op.construct(graph) for op in self.options]

		# print(f'opts {self} {opts}')
		poss = []
		for opt in opts:
			poss.extend(opt)

		return poss

		


class Symbol(object):
	"""docstring for Symbol"""
	def __init__(self, text):
		super(Symbol, self).__init__()
		# print(f'making Symbol from {text}')
		self.symbol = text.strip().strip('"')


	# always returns a string
	def construct(self, graph):
		return [self.symbol]
	

	def __str__(self):
		return f'Symbol: {self.symbol}'
	def __repr__(self):
		return str(self)
		

def construct_graph(rules):
	graph = {}
	for r in rules:
		loc, val = r.split(':')
		loc = int(loc)
		if '"' in val:
			graph[loc] = Symbol(val)  
		elif "|" in val:
			graph[loc] = Option(val)  
		else:
			graph[loc] = Seq(val)

	return graph


def is_matching_word(graph):

	return graph[0].construct(graph)


###
def get_rules(data):
	rules = []
	ii=0
	while data[0]:
		rules.append(data.pop(0))

	data.pop(0) # nuke the leading empty line
	return rules

def get_words(data):
	return data

def part1():
	data = read_data()

	rules = get_rules(data)
	words = get_words(data)

	graph = construct_graph(rules)
	strings = graph[0].construct(graph)
	# print(graph)

	# print('strings',)

	c = 0
	for w in words:
		if w in strings:
			c = c+1

	return c

###



def part2():
	data = read_data()
	thing = []
	for a in thing:
		pass

	return



print("part 1: {}".format(part1()))
# print("part 2: {}".format(part2()))
