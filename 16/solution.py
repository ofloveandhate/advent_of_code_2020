def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

class Field(object):
	"""docstring for Field"""
	def __init__(self, name, lower, upper):
		self.name = name

		self.lower = [int(a) for a in lower.split('-')]
		self.upper = [int(a) for a in upper.split('-')]

		
	def in_lower(self,t):
		return self.lower[0] <= t and t <= self.lower[1]

	def in_upper(self,t):
		return self.upper[0] <= t and t <= self.upper[1]

	def in_range(self,t):
		return self.in_lower(t) or self.in_upper(t)


def parse_fields(data):
	fields = []
	for ii in range(len(data)):
		d = data[ii]
		if len(d)==0:
			data = data[ii+1:]
			return fields, data
		name, ranges = d.split(":")
		lower, upper = ranges.split(" or ")
		fields.append(Field(name, lower, upper))

def parse_your_ticket(data):
	data.pop(0)
	my_ticket = data.pop(0)
	data.pop(0)
	return eval(f'[{my_ticket}]')


def parse_nearby_tickets(data):
	data.pop(0)
	
	return [eval(f'[{d}]') for d in data]

import numpy as np 

def error_invalid_ticket(ticket, fields):
	error = 0
	for v in ticket:
		validity = np.zeros( (len(fields)) )
		for ii in range(len(fields)):
			f = fields[ii]
			if f.in_range(v):
				validity[ii] = 1
		if sum(validity)==0:
			error = error+v

	return error

def part1():
	data = read_data()

	fields, data = parse_fields(data)

	my_ticket = parse_your_ticket(data)


	nearby_tickets = parse_nearby_tickets(data)


	c = 0
	for ticket in nearby_tickets:
		c = c+error_invalid_ticket(ticket, fields)


	return c


###



def part2():
	data = read_data()

	fields, data = parse_fields(data)

	my_ticket = parse_your_ticket(data)


	nearby_tickets = parse_nearby_tickets(data)



	valid_tickets = [t for t in nearby_tickets if error_invalid_ticket(t, fields)==0]
	print(len(valid_tickets))
	c = 0

	field_order = {}
	valid_tickets = [my_ticket] + valid_tickets
	from collections import Counter
	for f in fields:
		order = Counter()

		for ii in range(len(valid_tickets)):
			t = valid_tickets[ii]

			for jj in range(len(t)):
				v = t[jj]
				if f.in_range(v):
					print(f'{f.name} is valid on {t} at position {jj} {v}')
					order[jj] = order[jj]+1

		field_order[f.name] = order

	max_len_ticket = max( [len(t) for t in valid_tickets] )

	elim = np.zeros( (len(fields),  max_len_ticket) )

	fieldnames,counters = zip(*field_order.items())

	

	for ii in range(len(fields)):
		for k,v in counters[ii].items():
			elim[ii,k] = v

	useme = elim- (len(valid_tickets)-1)

	useme[np.where(useme<0)] = 0
	position = np.arange(max_len_ticket)


	final_orders = {}
	while len(final_orders) < len(fieldnames):
		print()
		print(useme)
		print(position)
		print("rowsum", np.sum(useme,1))
		rows = np.where(np.sum(useme,1)==1)[0]
		print("rows", rows)
		delme = []
		for row in rows:
			col = np.where(useme[row]==1)[0]
			print("rc",row, col)
			r = np.asscalar(row)
			c = np.asscalar(col)
			delme.append(c)
			print("row", r)
			print("col", c)
			print(f'{fieldnames[r]} = {c}')
			final_orders[fieldnames[r]] = position[c]

		useme = np.delete(useme, delme,1)
		position = np.delete(position, delme)

			# useme = np.delete(useme, r,0)
	p = 1
	for k,v in final_orders.items():
		if k.startswith('departure'):
			p = p*my_ticket[v]

	return p

# print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
