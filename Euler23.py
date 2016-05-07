def sum_divisors(n):
    """Sums the proper divisors of n."""
    sum = 1
    for x in xrange(2, int(n ** 0.5) + 1):
        if (n % x == 0):
            sum += x + n / x
    if (n ** 0.5) == int(n ** 0.5): sum -= (n ** 0.5)
    return sum

def is_abundant(n):
    """Checks if the sum of the divisors of n is greater than n."""
    if sum_divisors(n) > n: 
        return True
    else: return False

def find_abundants(limit):
    """Finds all abundant numbers up to the specified limit"""
    abundants = [x for x in xrange(1, limit) if is_abundant(x)]
    return abundants

def get_list(limit):
    abds = find_abundants(limit)
    list = range(limit)
    for x in abds:
        for y in abds:
            if x + y >= limit:
                break
            list[x + y] = 0
    return list

print sum(get_list(28123))