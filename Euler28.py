def spiral(side_size):
	"""Returns the sum of all the diagonals of a spiral of a given size."""
	count = 1
	tally = 0
	sum_of_numbers = 1
	for i in range(1, side_size+1):
		while tally < 4:
			count += (2 * i)
			sum_of_numbers += count
			tally += 1
		tally = 0
	return sum_of_numbers

print spiral(500)