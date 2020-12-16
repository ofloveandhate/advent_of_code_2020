def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###




def part1():
	data = read_data()
	acc = 0

	counts = set()

	line = 0
	
	while True:

		if line in counts:
			return acc

		instr = data[line]
		counts.add(line)

		op, val = instr.split()

		if op=="nop":
			line = line+1
		elif op=="acc":
			acc  = acc+int(val)
			line = line+1
		elif op=="jmp":
			line = line+int(val)


###

def run_that_shit(data):
	
	acc = 0

	counts = set()

	line = 0
	
	while True:

		if line in counts:
			raise ValueError("duplicate instruction encountered")

		try:
			instr = data[line]
		except:
			return acc

		counts.add(line)

		op, val = instr.split()

		if op=="nop":
			line = line+1
		elif op=="acc":
			acc  = acc+int(val)
			line = line+1
		elif op=="jmp":
			line = line+int(val)

	return acc

def mod_data(data, line):
	modded = data.copy()
	instr = data[line]
	op, val = instr.split()
	print(instr)
	if op=='nop':
		modded[line] = f"jmp {val}"
	elif op=='jmp':
		modded[line] = f"nop {val}"
	else:
		raise ValueError(f"line {line} not a candidate")
	
	return modded

def part2():
	data = read_data()

	line = 0
	while True:
		try:
			return run_that_shit(mod_data(data,line))
		except ValueError as e:
			line = line+1


print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
