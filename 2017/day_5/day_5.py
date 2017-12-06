with open ('input.txt') as input_file:
	puzzle_input = input_file.readlines()

def clean_up_input(puzzle_input):
	i = 0
	while(i < len(puzzle_input)):
		puzzle_input[i] = int(puzzle_input[i].strip('\n'))
		i += 1
	return puzzle_input

def step_through_instructions(puzzle_input):
	i = 0
	steps = 0

	while(i < len(puzzle_input)):
		i_value = puzzle_input[i]
		puzzle_input[i] += 1
		i += i_value
		steps += 1

	return steps

print(step_through_instructions(clean_up_input(puzzle_input)))