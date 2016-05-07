def distinct_powers():
	powers_list = []
	for a in range(2, 101):
		for b in range(2, 101):
			powers_list.append(a ** b)
	powers = list(set(powers_list))
	powers.sort()
	return len(powers)

print distinct_powers()