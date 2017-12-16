

puzzle_input = [18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188]
puzzle_input_string = "18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188"
suffix = [17, 31, 73, 47, 23]

def build_list(count):
	i = 0
	numbers = []
	while i < count:
		numbers.append(i)
		i+=1
	return numbers

def get_reversed_sublist(current_position, length, numbers_list):
	sublist = []
	i = current_position
	distance_so_far = 0
	while distance_so_far < length:
		if i >= len(numbers_list):
			i -= len(numbers_list)
		sublist.append(numbers_list[i])
		i+=1
		distance_so_far += 1
	sublist.reverse()
	return sublist

def replace_with_reversed_sublist(current_position, sublist, numbers_list):
	index_sub = 0
	index_main = current_position
	while index_sub < len(sublist):
		if index_main >= len(numbers_list):
			index_main = 0
		numbers_list[index_main] = sublist[index_sub]
		index_sub += 1
		index_main += 1
	return numbers_list

def tie_knots(instructions, current_position, skip_size, numbers_list):

	for instruction in instructions:
		sublist = get_reversed_sublist(current_position, instruction, numbers_list)
		numbers_list = replace_with_reversed_sublist(current_position, sublist, numbers_list)
		current_position = current_position + instruction + skip_size
		if current_position >= len(numbers_list):
			current_position = current_position % len(numbers_list)
		skip_size += 1

	return numbers_list, current_position, skip_size

def tie_more_knots(instructions, numbers_list, repeats):
	current_position = 0
	skip_size = 0
	times = 0

	while times < repeats:
		numbers_list, current_position, skip_size = tie_knots(instructions, current_position, skip_size, numbers_list)
		times += 1

	return numbers_list

def get_ascii(characters):
	asciis = []
	for c in characters:
		asciis.append(ord(c))
	return asciis

def append_suffix(original, suffix):
	for c in suffix:
		original.append(c)
	return original

def convert_to_xor(block):
	result = 0
	for piece in block:
		result ^= piece
	return result

def reduce_to_dense(block_size, sparse_hash):
	result = []
	block = []
	for item in sparse_hash:
		block.append(item)
		if len(block) == block_size:
			block_with_xor = convert_to_xor(block)
			result.append(block_with_xor)
			block = []
	return result

def convert_to_hexidecimal(hash):
	result = ''
	hex_to_add = ''
	for item in hash:
		hex_to_add = hex(item)[2:]
		if len(hex_to_add) == 1:
			hex_to_add = '0' + hex_to_add
		result += hex_to_add
	return result

print('Part 1:')
numbers = build_list(256)
alterned_list, current_position, skip_size = tie_knots(puzzle_input, 0, 0, numbers)
print(alterned_list[0] * alterned_list[1])

print('Part 2:')
numbers = build_list(256)
asciis = get_ascii(puzzle_input_string)
asciis = append_suffix(asciis, suffix)
knotted_64_times = tie_more_knots(asciis, numbers, 64)
reduced = reduce_to_dense(16, knotted_64_times)
hex = convert_to_hexidecimal(reduced)
print(hex)
print(len(hex))