def fibo( term ):
	if term == 1 or term == 2 :
		return term - 1
	else :
		first = 0
		second = 1
		next = first + second
		count = 3
		while count != term :
			first = second
			second = next
			next = first + second
			count += 1
		return next

def rfibo( term ):
	if term == 1 or term == 2 :
		return term - 1
	else :
		return rfibo( term - 2 ) + rfibo( term - 1 )
		
term = int(input(" Enter Term No : "))

print(" Fibonacci Element : ", fibo( term ))

print(" Fibonacci Element : ", rfibo( term ))