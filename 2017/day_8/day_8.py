with open ('input.txt') as input_file:
	puzzle_input = input_file.readlines()

registers = {}
highest_max = 0

def check_condition(register, operator, amount):
	result = False
	if operator == '>':
		if register > amount:
			result = True
	elif operator == '<':
		if register < amount:
			result = True
	elif operator == '>=':
		if register >= amount:
			result = True
	elif operator == '<=':
		if register <= amount:
			result = True
	elif operator == '==':
		if register == amount:
			result = True
	elif operator == '!=':
		if register != amount:
			result= True

	return result

def process_instruction(instruction, highest_max):
	instruction = instruction.split()

	if instruction[0] not in registers:
		registers[instruction[0]] = 0
	if instruction[4] not in registers:
		registers[instruction[4]] = 0

	if check_condition(registers[instruction[4]], instruction[5], int(instruction[6])):
		if(instruction[1]) == 'inc':
			registers[instruction[0]] = registers[instruction[0]] + int(instruction[2])
		else:
			registers[instruction[0]] = registers[instruction[0]] - int(instruction[2])

	new_max = max(registers.values())
	if new_max > highest_max:
		highest_max = new_max
	return highest_max

for instruction in puzzle_input:
	highest_max = process_instruction(instruction, highest_max)

print(max(registers.values()))
print(highest_max)
