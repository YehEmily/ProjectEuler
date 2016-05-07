def is_narcissistic(n, power):
	"""Returns the number if it is narcissistic, or 0 if otherwise."""
	sum_of_numbers = 0
	numbers = [int(i) for i in str(n)]
	for digit in numbers:
		sum_of_numbers += digit ** power
	if sum_of_numbers == n:
		print sum_of_numbers
		return sum_of_numbers
	else:
		return 0

def fifth_powers(power):
	"""Returns the sum of all narcissistic numbers for a given power."""
	sum_of_numbers = 0
	for i in range(2, 1000000):
		sum_of_numbers += is_narcissistic(i, power)
	return sum_of_numbers

print fifth_powers(5)