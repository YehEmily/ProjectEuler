dict_pentagonal = {}
dict_hexagonal = {}

pentagonal_n = 165
hexagonal_n = 143

def generate_triangle(n):
	return n * (n + 1) / 2

def generate_pentagonal(n):
	return n * (3 * n - 1) / 2

def generate_hexagonal(n):
	return n * (2 * n - 1)

def is_pentagonal(target):
	global pentagonal_n
	global hexagonal_n

	if target in dict_pentagonal:
		return True
	else:
		pentagon_val = generate_pentagonal(pentagonal_n)
		dict_pentagonal[pentagon_val] = True
		while (pentagon_val <= target):
			if (pentagon_val == target):
				return True
			else:
				pentagonal_n += 1
				pentagon_val = generate_pentagonal(pentagonal_n)
				dict_pentagonal[pentagon_val] = True
	return False

def is_hexagonal(target):
	global pentagonal_n
	global hexagonal_n

	if target in dict_hexagonal:
		return True
	else:
		hexagon_val = generate_hexagonal(hexagonal_n)
		dict_hexagonal[hexagon_val] = True
		while (hexagon_val <= target):
			if (hexagon_val == target):
				return True
			else:
				hexagonal_n += 1
				hexagon_val = generate_hexagonal(hexagonal_n)
				dict_hexagonal[hexagon_val] = True
	return False


bool_is_pentagonal = False
bool_is_hexagonal = False
triangle_n = 285

while (not bool_is_pentagonal or not bool_is_hexagonal):
	triangle_n += 1
	target = generate_triangle(triangle_n)
	bool_is_pentagonal = is_pentagonal(target)
	bool_is_hexagonal = is_hexagonal(target)
	print(bool_is_pentagonal, bool_is_hexagonal)

print(triangle_n, pentagonal_n, hexagonal_n)
print(generate_triangle(triangle_n), generate_pentagonal(pentagonal_n), generate_hexagonal(hexagonal_n))
print(triangle_n)

