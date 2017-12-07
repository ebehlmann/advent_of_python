with open ('input.txt') as input_file:
	puzzle_input = input_file.readlines()

def process_input(puzzle_input):
	split = puzzle_input[0].split("\t")
	as_int = []
	for item in split: 
		as_int.append(int(item))
	return as_int

def find_first_max_bank(bank_config):
	max_index = 0
	max_bank = 0
	i = 0
	while(i<len(bank_config)):
		if bank_config[i] > max_bank:
			max_index = i
			max_bank = bank_config[i]
		i += 1
	return max_index

def redistribute_blocks(starting_config):
	past_configs = []

	current_config = starting_config
	past_configs.append(list(current_config))
	
	redistributions = 0

	while(True):
		max_bank = find_first_max_bank(current_config)
		blocks_to_redistribute = current_config[max_bank]
		current_config[max_bank] = 0

		if(max_bank == len(current_config) - 1):
			position = 0
		else:
			position = max_bank + 1

		while blocks_to_redistribute > 0:
			current_config[position] += 1
			if(position == len(current_config) - 1):
				position = 0
			else:
				position = position + 1

			blocks_to_redistribute -= 1

		redistributions += 1

		if(current_config in past_configs):
			break
		else:
			past_configs.append(list(current_config))

	return redistributions

cleaned_input = process_input(puzzle_input)
print(redistribute_blocks(cleaned_input))