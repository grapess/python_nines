num = int( input(" Enter Any Number : "))

isprime = True

div = 2
range = num - 1
while div <= range :
	if num % div == 0 :
		isprime = False
	div += 1

if isprime :
	print(" Given Number is Prime ")
else :
	print(" Given Number is Composite ")