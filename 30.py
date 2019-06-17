sum = 0

while True :
	num = int(input(" Enter Any Number : "))
	sum = sum + num
	print(" Press 1 For Add Another Number ")
	choice = int( input(" Enter your Choice : "))
	if choice != 1 :
		break

print(" Given Number Sum : " , sum )