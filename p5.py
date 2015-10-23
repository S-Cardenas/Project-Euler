def divisible(mini, maxi):
	divisors = range(mini, maxi + 1)
	number = 1
	while True:
		print number
		remainders = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for i in range(mini, maxi + 1):
			remainders[i - 1] = number % divisors[i - 1]
		if sum(remainders) == 0:
			print "Smallest positive number is: ", number
			break
		number += 1.0

divisible(1, 20)