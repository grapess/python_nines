
num = int(input(" Enter Any Number : "))

temp = num

if temp < 0 :
	temp = temp * -1

sum = 0

while temp != 0 :
	rem = temp % 10
	sum = sum + rem
	temp = temp // 10
	
print(" Sum of Digit of Given Number : " , sum )