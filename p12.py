import itertools

def triangle_divisors(goal):
	
	triangle = 0
	indices = 1
	num_divisors = []
	
	while len(num_divisors) <= goal:
		
		triangle += indices
		print triangle
		num_divisors = []
		
		for divisor in itertools.count(1):
			if divisor <= triangle:
				if triangle % divisor == 0:
					num_divisors.append(divisor)
			else:
				break
		
		indices += 1
		
	print "Number of units added: ", indices - 1
	print "Triangle is:", triangle
	print "The multiples are:\n", num_divisors
	print "With a length of:", len(num_divisors)

	
triangle_divisors(500)

	
	