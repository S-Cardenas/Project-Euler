def squares(n):
	i = 1 
	sum_sq = 0
	while i <= n:
		sum_sq += i ** 2
		i += 1
	print sum_sq
	
	list = range(1, n + 1)
	sq_sum = (sum(list)) ** 2
	print  sq_sum
	
	print "The difference between the sum of the squares of the first %d" % n
	print "natural numbers and the square of the sum: ", (sq_sum - sum_sq)

squares(100)