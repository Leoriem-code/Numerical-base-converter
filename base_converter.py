characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
dictionary = {}
for i in range(95):
	dictionary[characters[i]] = str(i)
	dictionary[str(i)] = characters[i]

def transformation(value):
	"""value is a string or a list of string
	return a list"""
	global dictionary
	result = []
	for i in value:
		result.append(dictionary[i])
	return result

def convert(value, starting_base = 10, arrival_base = 10):
	"""Convert 'value' written in 'starting_base' in numerical base 'arrival_base' (both 10 by default).
	Works with numerical base from 2 to 96. Use the string.printable[:95] for the symbols
	'value' in a string or a list of string
	'arrival_base' and 'starting_base' are integer"""

	if starting_base != 10:
		value = transformation(value)
		a = [int(i) for i in value]
		a.reverse()
		result = 0
		for ind in range(len(a)):
			i = a[ind]
			result += i* (starting_base**ind)
		value = str(result)

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
		value = "".join(transformation(result))
	return value
