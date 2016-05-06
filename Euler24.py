import itertools

def permutations(numbers_list, n):
	permutation_list = list(itertools.permutations(numbers_list, n))
	return permutation_list[999999]

print permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)