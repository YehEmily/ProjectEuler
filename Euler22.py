alpha_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

def names_list(file_name):
	f = open(file_name,'r')
	names = f.readlines()
	for name in names:
		split_names = name.split('","')
	list_names = [name.strip('"') for name in split_names]
	list_names.sort()
	return list_names

def total_names(file_name):
	list_names = names_list(file_name)
	total = 0
	for name in list_names:
		letters_sum = 0
		for letter in name:
			letters_sum += alpha_dict[letter]
		total += (letters_sum * (list_names.index(name)+1))
	return total


print total_names("names.txt")