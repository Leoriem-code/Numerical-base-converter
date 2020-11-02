characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
dictionary = {}
for i in range(len(characters)):
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


def convert(value, base_start =10, base_end =10):
	"""Convert 'value' written in 'base_start' in base 'base_end' (both 10 by default).
	Works with numerical base from 2 to 96. Use the string.printable[:95] for the symbols.
	'value' is a string
	'base_end' and 'base_start' are integer
	return a string"""

	value = str(value)
	if value[0] == '-':
		value = value[1:]
		negative = True
	else:
		negative = False

	if base_start != 10:
		value = transformation(value)
		a = [int(i) for i in value]
		a.reverse()
		result = 0
		for ind in range(len(a)):
			coeff = a[ind]
			result += coeff* (base_start**ind)
		value = str(result)

	if base_end != 10:
		value = int(value)
		limite = 0
		buff = value
		while buff//base_end != 0:
			limite += 1
			buff = buff//base_end
		result = []
		for j in range(limite, -1, -1):
			nbr = base_end**j
			diff = value - nbr
			fois = diff//nbr +1
			value = value - nbr*fois
			result.append(str(fois))
		value = "".join(transformation(result))

	if negative:
		value = '-%s' %value
	return value


def base(values, starting_base =10, arrival_base =10):
	"""Convert 'values' written in 'starting_base' in base 'arrival_base' (both 10 by default).
	Works with numerical base from 2 to 96. Use the string.printable[:95] for the symbols.
		'value' is a string or a list (or a tuple) of values to convert
		'starting_base' and 'arrival_base' are integer
		return a value of the type of values 
			(values is a string, return a string; same for list or tuple)"""

	if starting_base <2 or arrival_base <2 or starting_base >96 or arrival_base >96:
		print("Error.\nValue of Base between 2 and 96. Please trye again with a different value")
		return None
	if type(values) == type(float()):
		print("W(hy)tf does a float is here?")
		return None

	if type(values) == type(str()):
		val_convert = convert(values, starting_base, arrival_base)
		return val_convert

	if type(values) == type(list()) or type(values) == type(tuple()):
		result = []
		for sub_values in values:
			if type(sub_values) == type(str()) or type(sub_values) == type(int()):
				number = str(sub_values)
			else:
				number = sub_values[0]
				starting_base = sub_values[1]
				arrival_base = sub_values[2]
			result.append(convert(number, starting_base, arrival_base))
		return result
	
