def line(symbol,times):
	result = ""
	count = 1
	while count <= times:
		result += str(symbol)
		count += 1
	print(result)
	
line('=',30)
print(" Hello ")
line('~',40)
print(" Grapess ")
line('_',45)
print(" Solutions ")
line('-',50)