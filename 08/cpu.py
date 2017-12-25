class Registers(dict):
	def __missing__(self, key):
		value = self[key] = 0
		return value

def eval_condition(condition, registers):
	register, operator, value = condition.split(' ')
	return eval(f'{registers[register]}{operator}{value}')
with open('input.txt') as infile:
	r = Registers()
	largest = 0
	for line in infile.readlines():
		line = line.strip()
		setvalue, condition = line.split(' if ')
		if eval_condition(condition, r):
			regname, inc, value = setvalue.split(' ')
			if inc == 'inc':
				r[regname] += int(value)
			else:
				r[regname] -= int(value)
			if r[regname] > largest:
				largest = r[regname]
	print(r)
	print(largest)
