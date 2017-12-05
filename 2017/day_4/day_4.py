def alphabetize_letters(word):
	letters = list(word)
	sorted_letters = sorted(letters)
	return ''.join(sorted_letters)

def check_for_validity(passphrase, problem_number):
	if(problem_number == 2):
		k = 0
		while(k<len(passphrase)):
			passphrase[k] = alphabetize_letters(passphrase[k])
			k += 1

	i = 0
	j = 0

	while(i<len(passphrase)):
		while(j<len(passphrase)):
			if(i != j):
				if(passphrase[i] == passphrase[j]):
					return False
			j += 1
		i += 1
		j = 0

	return True

with open ('input.txt') as input_file:
	input = input_file.readlines()

count1 = 0
count2 = 0

for passphrase in input:
	words = passphrase.split()
	result1 = check_for_validity(words, 1)
	if result1 == True:
		count1 += 1

	result2 = check_for_validity(words, 2)
	if result2 == True:
		count2 += 1

print(count1)
print(count2)