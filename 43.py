num = int( input(" Enter Any Number : "))

result = ""
sum = 0
temp = num
last_digit = True

if temp < 0 :
	temp = temp * -1
	
while temp > 0 :
	rem = temp % 10
	if last_digit :
		result = str( rem ) + result
		last_digit = False
	else:
		result = str( rem ) + " + " + result
	temp = temp // 10
	sum = sum + rem
	
result = " [ " + result + " = " + str(sum) + " ]"
	
print( result )