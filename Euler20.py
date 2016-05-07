import math

def sum_of_factorial_digits(n):
	"""Returns the sum of the digits in a number after computing its factorial."""
	x = str(math.factorial(n))
	digits = [int(number) for number in x]
	sum_digits = sum(digits)
	return sum_digits

print sum_of_factorial_digits(100)