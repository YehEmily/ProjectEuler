def len_fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return len(str(a))

def index_1000():
	for n in range(1000, 10000):
		if len_fib(n) == 1000:
			return n
		else:
			pass

print index_1000()