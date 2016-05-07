def sum_factors(n):
	"""Computes the sum of the factors of a given number n."""
	sum_factors = 0
	for i in range(1, n):
		if n % i == 0:
			sum_factors += i
	return sum_factors

def amicable_numbers(n):
	"""Determines whether a pair of numbers a, b in range n is amicable and returns their sum."""
	total = 0
	for r in range(n):
		a = sum_factors(r)
		b = sum_factors(a)
		if a != b and b == r:
			total += r
	return total

print sum_factors(284)
print amicable_numbers(10000)