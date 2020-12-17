def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

class Instruction(object):
	"""docstring for Instruction"""
	def __init__(self, text):
		super(Instruction, self).__init__()
		a,b = text.split(' = ')

		print(a)
		self.loc = int(a.strip('mem[').strip(']'))
		self.val = int(b)


	def __str__(self):
		return f'[{self.loc}] = val'
	def __repr__(self):
		return str(self)
		


# destructively produces a mask and instructions
def process_next_program(code):
	mask = code.pop(0)
	instructions = []
	while len(code)>0 and not code[0].startswith('mask'):
		instructions.append(Instruction(code.pop(0)))

	return mask, instructions

def result(mask, val):
	as_bin = '{0:036b}'.format(val)
	r = ''
	for m,b in zip(mask, as_bin):
		if m=='0':
			r = r+'0'
		elif m=='1':
			r = r+'1'
		else:
			r = r+b

	print(f'val as bin: {as_bin}')
	print(f'mask      : {mask}')
	print(f'r         : {r}\n')
	return int(r,2)

class Program(object):
	"""docstring for Program"""
	def __init__(self, code):
		super(Program, self).__init__()

		mask, instructions = process_next_program(code)

		self.mask = mask.strip('mask = ')
		self.instructions = instructions
	
	def __str__(self):
		return f'Program with mask {self.mask} and {len(self.instructions)} instructions'

	def execute(self, memory):
		for I in self.instructions:
			memory[I.loc] = result(self.mask, I.val)

class Computer(object):
	"""docstring for Computer"""
	def __init__(self, data):
		self.data = data

		self.programs = []
		while len(data):
			self.programs.append(Program(data))

		self.memory = {}

	def execute(self):
		for p in self.programs:
			p.execute(self.memory)


	def __str__(self):
		s = f'Computer with {len(self.programs)} program(s):\n'
		for p in self.programs:
			s = s+str(p)+'\n'

		return s
	def report(self):
		return sum(self.memory.values())

def part1():
	data = read_data()

	c = Computer(data)
	c.execute()
	return c.report()



###



def part2():
	data = read_data()
	thing = []
	for a in thing:
		pass

	return

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
