

def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return data

def part1():
	data = read_data()

	count = 0

	for d in data:
		span,letter,password = d.split()
		lower,upper = span.split('-')
		letter = letter[0]
		occ = password.count(letter)

		if int(lower) <= occ and occ <= int(upper):
			count = count+1

	return count


def part2():
	data = read_data()

	count = 0

	for d in data:
		span,letter,password = d.split()
		pos1,pos2 = span.split('-')
		letter = letter[0]

		if (password[int(pos1)-1]==letter) != (password[int(pos2)-1] == letter):
			count = count+1

	return count

print(part1())
print(part2())