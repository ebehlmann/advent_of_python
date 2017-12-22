import random

with open ('input.txt') as input_file:
	puzzle_input = input_file.readlines()

def process_input(puzzle_input):
	programs = {}
	for line in puzzle_input:
		line = line.split()

		connected_programs = []
		i = 2
		while i < len(line):
			line[i] = line[i].replace(',', '')
			connected_programs.append(int(line[i]))
			i += 1

		programs[int(line[0])] = connected_programs
	return programs

def find_connected_with(programs, program_to_check):
	connected_programs = []
	add_this_round = []
	added_last_round = [program_to_check]
	connected_programs.append(program_to_check)

	keep_going = True

	while keep_going == True:
		for i in added_last_round:
			to_add = programs[i]
			for j in to_add:
				if j not in connected_programs:
					connected_programs.append(j)
					add_this_round.append(j)

		if len(add_this_round) == 0:
			keep_going = False
		else:
			added_last_round = add_this_round
			add_this_round = []

	return connected_programs

def find_distinct_groups(programs):
	groups = 0
	while len(programs) > 0: 
		program_to_check = random.choice(list(programs.keys()))
		program_group = find_connected_with(programs, program_to_check)
		if len(program_group) > 0:
			groups += 1
		for program in program_group:
			programs.pop(program, None)
	return groups

programs = process_input(puzzle_input)
print('Part 1:')
connected_programs = find_connected_with(programs, 0)
print(len(connected_programs))

print('Part 2:')
print(find_distinct_groups(programs))
