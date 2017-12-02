def separate_numbers(row):
	numbers = row.split("\t")
	for number in numbers:
		number.replace("/n", "")
	return numbers

def find_diff(row_as_array):
	min = int(row_as_array[0])
	max = int(row_as_array[0])

	for number in row_as_array:
		if int(number) < min:
			min = int(number)

		if int(number) > max:
			max = int(number)

	return max-min

def find_quotient_of_divisibles(row_as_array):
	i=0
	quotient = 0

	while(i < len(row_as_array)):
		j = 0
		while(j < len(row_as_array)):
			first = int(row_as_array[i])
			second = int(row_as_array[j])
			print(first, second)
			if(first != second and first % second == 0):
				quotient = first / second
				break
			j += 1
		i += 1
	print(quotient)
	return quotient

# input is an array of strings
def find_checksum_one(input):
	checksum = 0

	for row in input:
		numbers = separate_numbers(row)
		diff = find_diff(numbers)
		checksum += diff

	return checksum

def find_checksum_two(input):
	checksum = 0

	for row in input:
		numbers = separate_numbers(row)
		quotient = find_quotient_of_divisibles(numbers)
		checksum += quotient

	return checksum	

with open ('input.txt') as input_file:
	input = input_file.readlines()
	
print(find_checksum_one(input))
print(find_checksum_two(input))