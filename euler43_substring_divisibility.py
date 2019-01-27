import itertools

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

raw_perms = itertools.permutations(digits, 10)
perms = []

def is_interesting(perm):
	if int(perm[0]) == 0:
		return False

	if int(str(perm[1]) + str(perm[2]) + str(perm[3])) % 2 != 0:
		return False
	if int(str(perm[2]) + str(perm[3]) + str(perm[4])) % 3 != 0:
		return False
	if int(str(perm[3]) + str(perm[4]) + str(perm[5])) % 5 != 0:
		return False
	if int(str(perm[4]) + str(perm[5]) + str(perm[6])) % 7 != 0:
		return False
	if int(str(perm[5]) + str(perm[6]) + str(perm[7])) % 11 != 0:
		return False
	if int(str(perm[6]) + str(perm[7]) + str(perm[8])) % 13 != 0:
		return False
	if int(str(perm[7]) + str(perm[8]) + str(perm[9])) % 17 != 0:
		return False
	return True

for perm in raw_perms:
	if (is_interesting(perm) == True):
		perms.append(perm)

final_results = []

for perm in perms:
	joined = ''.join(str(digit) for digit in perm)
	final_results.append(int(joined))

print(final_results)
print(sum(final_results))