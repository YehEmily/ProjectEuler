def generateDigit(n):
	string = ''
	i = 1
	while (len(string) < n):
		string += str(i)
		i += 1
	return string

bigNumber = generateDigit(1000000)
d_1 = int(bigNumber[0])
d_10 = int(bigNumber[9])
d_100 = int(bigNumber[99])
d_1000 = int(bigNumber[999])
d_10000 = int(bigNumber[9999])
d_100000 = int(bigNumber[99999])
d_1000000 = int(bigNumber[999999])

print(d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000)