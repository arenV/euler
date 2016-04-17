'''
Author: Aren Voorhees
Date: 04/17/2016
Program Name: Sum of multiples
Input: 10
Output: 23
'''

def multiples(x):
	total = 0
	for i in range(1, x):
		if i % 3 == 0 or i % 5 == 0:
			total += i
	return total

print (multiples(1000))
