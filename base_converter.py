from string import printable
printable = printable[:10] + printable[36:62] + printable[10:36] + printable[62:]

dictionary = {}
for i in range(95):
	dictionary[printable[i]] = str(i)
	dictionary[str(i)] = printable[i]

def conv(value):
	"""value is a string or a list of string"""
	global dictionary
	result = []
	for i in value:
		result.append(dictionary[i])
	return "".join(result)


def decomp(value, starting_base = 10, arrival_base = 10):
	"""Convert 'value' written in 'starting_base' in base 'arrival_base' (both by default 10).
	Works with numerical base from 2 to 96. Use the string.printable[:95] for the symbols
	'value' in a string or a list of string
	'arrival_base' and 'starting_base' are integer"""

	value = conv(value)
	if starting_base != 10:
		result = 0
		if starting_base > 10 or len(value.split(" ")) != 1:
			a = [int(i) for i in value.split(" ")]
		else:
			a = [int(i) for i in value]
		a.reverse()
		for i in a:
			ind = a.index(i)
			result += i* (starting_base**ind)
			a[ind] = i-1
		value = conv(str(result))

	if arrival_base != 10:
		value = int(value)
		limite = 0
		buff = value
		while buff//arrival_base != 0:
			limite += 1
			buff = buff//arrival_base

		result = []
		for j in range(limite, -1, -1):
			nbr = arrival_base**j
			diff = value - nbr
			fois = diff//nbr +1
			value = value - nbr*fois
			result.append(str(fois))
		value = conv(result)
	return value