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

		self.loc = int(a.strip('mem[').strip(']'))
		self.val = int(b)


	def __str__(self):
		return f'[{self.loc}] = {self.val}'
	def __repr__(self):
		return str(self)
		


# destructively produces a mask and instructions
def init_next_program(code):
	mask = code.pop(0)
	instructions = []
	while len(code)>0 and not code[0].startswith('mask'):
		instructions.append(Instruction(code.pop(0)))

	return mask, instructions

def val_result(mask, val):
	as_bin = '{0:036b}'.format(val)
	r = ''
	for m,b in zip(mask, as_bin):
		if m=='0':
			r = r+'0'
		elif m=='1':
			r = r+'1'
		else:
			r = r+b

	return int(r,2)

class Program(object):
	"""docstring for Program"""
	def __init__(self, code):
		super(Program, self).__init__()

		mask, instructions = init_next_program(code)

		self.mask = mask.strip('mask = ')
		self.instructions = instructions
	
	def __str__(self):
		return f'Program with mask {self.mask} and {len(self.instructions)} instructions'

	def execute(self, memory):
		for I in self.instructions:
			memory[I.loc] = val_result(self.mask, I.val)

	def execute2(self,memory):
		print(f'\nmask: {self.mask}')
		for I in self.instructions:
			print(f'executing instruction {I}')

			loc = '{0:036b}'.format(I.loc)



			for ii in range(2**self.mask.count('X'),-1,-1):
				print(f'iteration {ii}')
				fmt = '{:0'+str(self.mask.count('X'))+'b}'
				as_bin = fmt.format(ii)
				dest = ''
				
				for m,ell in zip(self.mask, loc):

					if m=='X':
						dest = dest+as_bin[0]
						if len(as_bin):
							as_bin = as_bin[1:]
					elif m=='0':
						dest = dest+ell
					elif m=='1':
						dest = dest+'1'
					else:
						raise ValueError()
						

				print(f'dest:  {dest}')
				
				dest = int(dest,2)
				print(f'[{dest}] = {I.val}')
				memory[dest] = I.val

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

	def execute2(self):
		for p in self.programs:
			p.execute2(self.memory)


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

	c = Computer(data)
	c.execute2()
	return c.report()

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
