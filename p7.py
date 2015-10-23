import math

def prime_numbers(n):
	primes = [2, 3]
	number = 3.0
	while len(primes) < n:
		number += 1
		max_divisor = math.ceil(math.sqrt(number))
		if max_divisor < 3.0:
			max_divisor = 3.0
		divisors = range(2, int(max_divisor + 1))
		remainders = []
		for di in divisors:
			remainders.append(number % di)
		if 0 not in remainders:
			primes.append(number)
	print primes
	print "The last prime is: ", primes[-1]	

prime_numbers(10001)

