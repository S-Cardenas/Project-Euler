def fib_even(max):
	fib = [1, 2]
	i = 1
	while True:
		if (fib[i - 1] + fib[i]) <= max:
			fib.append((fib[i - 1] + fib[i]))
			i += 1
		else:
			print fib
			break
	
	even = []
	for number in fib:
		if number % 2.0 == 0:
			even.append(number)
	sums = sum(even)
	print sums
	
fib_even(4000000)
