def check_prime( num ) :
	div = 2
	range = num // 2
	while div <= range :
		if num % div == 0 :
			return False
		div += 1
	return True

def rcheck_prime( num , div , range ) :	
	if div <= range :
		if num % div == 0 :
			return False
		return rcheck_prime( num , div + 1 , range )
	else :
		return True
	
num = int(input(" Enter Any Number : "))

if check_prime( num ) :
	print(" Given Number is Prime ")
else :
	print(" Give Number is Composite ")
	
if rcheck_prime( num , 2 , num // 2 ) :
	print(" Given Number is Prime ")
else :
	print(" Give Number is Composite ")