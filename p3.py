def prime_factors(n):
	#Returns the largest prime factors of a positive integer
	factors = []
	d = 2
	while n > 1:
		while n % d == 0:
			factors.append(d)
			n /= d
		d = d + 1
	print factors
	print "The largest factor is:", max(factors)
	
prime_factors(600851475143)