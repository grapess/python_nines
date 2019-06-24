num = int( input(" Enter Any Number : "))

temp = num

if temp < 0 :
	temp = temp * -1
	
rev = 0
while temp > 0 :
	rem = temp % 10
	rev = rev * 10 + rem
	temp = temp // 10
	
if num < 0 :
	rev = rev * -1

print(" Reverse of Given Number : " , rev)