#Returns the 'palindrome' of a number
def palindrome(num):
    return str(num)[::-1]

#Finds the maximum palindrome from a multiplication of two 3-digit numbers
def max_palindrome(mini, maxi):
	set1 = range(mini, maxi)
	set2 = range(mini, maxi)
	palis = []
	for number1 in set1:
		for number2 in set2:
			prod = number1 * number2
			if (number1 * number2) == int(palindrome(prod)):
				palis.append(prod)
	print palis
	print "Largest palindrome is: ", max(palis)
	
max_palindrome(100, 1000)