def multiples(max, num1, num2):
	list = []
	for integer in range(max):
		if (float(integer) % num1 == 0) or (float(integer) % num2 == 0):
			list.append(integer)
	ans = sum(list)
	print "The sum of the multiples is:", ans
	print list

	
multiples(1000, 3, 5)	