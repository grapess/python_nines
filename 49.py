import math
num = int( input(" Enter Any Number : "))

isprime = True
count = 0

if num % 2 == 0 :
	isprime = False
	count = 1
else:
	count = 1
	div = 3
	range = math.sqrt( num )

	while div <= range :
		count += 1
		if num % div == 0 :
			isprime = False
			break
		div += 2

if isprime :
	print(" Given Number is Prime ")
else :
	print(" Given Number is Composite ")
	
print(" Total Count : " , count )