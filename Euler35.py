def find_factors(x):
	"""Computes the factors of a number x."""
	factors = []
	for i in range(1, x + 1):
		if x % i == 0:
			factors.append(i)
	return factors

def primes(n):
    """Returns  a list of primes in range n."""
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def find_circular_primes(r):
	"""Calculates the number of circular primes in range r."""
	prime = primes(r)
	circular_primes = 0
	for n in prime:
		string = str(n)
		if len(string) == 1:
			circular_primes += 1
		elif len(string) == 2:
			if int(string[1] + string[0]) in prime:
				circular_primes += 1
		elif len(string) == 3:
			if int(string[1] + string[2] + string[0]) in prime and int(string[2] + string[0] + string[1]) in prime:
				circular_primes += 1
		elif len(string) == 4:
			if int(string[1] + string[2] + string[3] + string[0]) in prime and int(string[2] + string[3] + string[0] + string[1]) in prime and int(string[3] + string[0] + string[1] + string[2]) in prime:
				circular_primes += 1
		elif len(string) == 5:
			if int(string[1] + string[2] + string[3] + string[4] + string[0]) in prime and int(string[2] + string[3] + string[4] + string[0] + string[1]) in prime and int(string[3] + string[4] + string[0] + string[1] + string[2]) in prime and int(string[4] + string[0] + string[1] + string[2] + string[3]) in prime:
				circular_primes += 1
		else:
			if int(string[1] + string[2] + string[3] + string[4] + string[5] + string[0]) in prime and int(string[2] + string[3] + string[4] + string[5] + string[0] + string[1]) in prime and int(string[3] + string[4] + string[5] + string[0] + string[1] + string[2]) in prime and int(string[4] + string[5] + string[0] + string[1] + string[2] + string[3]) in prime and int(string[5] + string[0] + string[1] + string[2] + string[3] + string[4]) in prime:
				circular_primes += 1
	return circular_primes



# print find_factors(18)
# print find_primes(1000000)
print find_circular_primes(1000000)