def self_powers(n):
	total = 0
	for i in range(1, n+1):
		total += i**i
	digits = list(str(total))
	final_10_digits = digits[-10:]
	return final_10_digits

print self_powers(1000)