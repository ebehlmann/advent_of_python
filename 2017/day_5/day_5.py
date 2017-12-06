def clean_up_input(puzzle_input):
	i = 0
	while(i < len(puzzle_input)):
		puzzle_input[i] = int(puzzle_input[i].strip('\n'))
		i += 1
	return puzzle_input

def step_through_instructions(puzzle_input, part):
	i = 0
	steps = 0

	while(i < len(puzzle_input)):
		i_value = puzzle_input[i]
		if(part == 1):
			puzzle_input[i] += 1
		else:
			if(puzzle_input[i] >= 3):
				puzzle_input[i] -= 1
			else: 
				puzzle_input[i] += 1
		i += i_value
		steps += 1

	return steps

with open ('input.txt') as input_file:
	puzzle_input = input_file.readlines()

cleaned_input = clean_up_input(puzzle_input)

print('Part 1:')
print(step_through_instructions(cleaned_input, 1))

# reset everything 
with open ('input.txt') as input_file:
	puzzle_input = input_file.readlines()

cleaned_input = clean_up_input(puzzle_input)

print('Part 2:')
print(step_through_instructions(cleaned_input, 2))