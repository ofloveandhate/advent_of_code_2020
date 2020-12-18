def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###



def parser(line):
	from simpleeval import simple_eval
	import simpleeval
	import ast
	import operator
	s = simpleeval.SimpleEval()
	s.operators[ast.Sub] = operator.mul

	line = line.replace('*','-')
	return s.eval(line)




def part1():
	data = read_data()

	s = 0
	for ii in range(len(data)):
		d = data[ii]
		s = s+ parser(d)

	return s


###


def parser2(line):
	from simpleeval import simple_eval
	import simpleeval
	import ast
	import operator
	s = simpleeval.SimpleEval()
	s.operators[ast.Sub] = operator.mul
	s.operators[ast.Div] = operator.add

	line = line.replace('*','-')

	line = line.replace('+','/')
	return s.eval(line)


def part2():
	data = read_data()

	s = 0
	for ii in range(len(data)):
		d = data[ii]
		s = s+ parser2(d)

	return s

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
