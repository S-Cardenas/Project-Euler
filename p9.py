import math		

def pyth_trip(big):
	a = range(2, big + 1)
	b = range(2, big + 1)
	triplets = []
	i = 0
	for num_a in a:
		i += 1
		for num_b in b[i:]:
			c = math.sqrt(num_a**2 + num_b**2)
			if (c).is_integer():
				triplets.append([num_a, num_b, c])
	for trips in triplets:
		if sum(trips) == big:
			print trips
		
	
pyth_trip(1000)