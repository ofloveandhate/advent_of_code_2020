import numpy as np

def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')



def c_byr(val):
	if len(val)==4 and int(val)>=1920 and int(val) <=2002:
		return True
	else:
		return False

def c_iyr(val):
	if len(val)==4 and int(val)>=2010 and int(val) <=2020:
		return True
	else:
		return False

def c_eyr(val):
	if len(val)==4 and int(val)>=2020 and int(val) <=2030:
		return True
	else:
		return False

def c_hgt(val):
	if val.endswith('cm'):
		q = int(val.strip('cm'))
		if (150 <= q) and (q <= 193):
			return True
		else:
			return False
	if val.endswith('in'):
		q = int(val.strip('in'))
		if (59 <= q) and (q <= 76):
			return True
		else:
			return False
	return False

def c_ecl(val):
	if val in ['amb','blu','brn','gry','grn','hzl','oth']:
		return True
	else:
		return False

def c_hcl(val):
	if val.startswith('#') and len(val)==7:	
		for v in val[1:]:
		 	if v not in '0123456789abcdef':
		 		return False
		return True

	return False

def c_pid(val):
	if len(val)==9:
		for v in val:
		 	if v not in '0123456789':
		 		return False

		return True

	return False

def c_cid(val):
	return True


fields =      ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
constraints = [c_byr,c_iyr,c_eyr,c_hgt,c_hcl,c_ecl,c_pid,c_cid]
fn_lookup = dict(zip(fields,constraints))
assert(len(fields)==len(constraints))



def detect_all_fields(record):
	have = np.zeros(len(fields))
	for ii in range(len(fields)):
		if fields[ii] in record:
			have[ii] = 1

	if sum(have[:-1])==(len(fields)-1):
		return True

	return False

def part1():
	data = read_data()
	this_record = ""
	counter = 0
	for ii in range(len(data)):
		d = data[ii]

		if len(d)>0:
			this_record = this_record+" "+d
		if not d or ii==len(data):
			if detect_all_fields(this_record):
				counter = counter +1

			this_record = ""
			# end of record

	return counter




def neccesary_fields_valid(have):
	for f in fields[:-1]:
		if not have[f]:
			return False
	return True

def field_processing(this_record):
	pieces = this_record.split()
	have = dict(zip(fields,[False]*len(fields)))

	c = 0
	q = []
	for p in pieces:
		a,b = p.split(':')

		if a in q:
			raise ValueError('duplicate key')
		q.append(a)

		f = fn_lookup[a]
		if f(b):
			have[a] = True
			
		c = c+1

	if neccesary_fields_valid(have):
		return True
	else:
		return False

def part2():
	data = read_data()
	this_record = ""
	counter = 0
	for ii in range(len(data)):
		d = data[ii]

		if len(d)>0:
			this_record = this_record+" "+d

		if not d or ii==(len(data)-1):
			if field_processing(this_record):
				counter = counter +1

			this_record = ""
			# end of record

	return counter

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))













