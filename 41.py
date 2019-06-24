diff = 3
value = 0
count = 1
result = ""
while count <= 15 :
	result += " " + str(value)
	value = value + diff
	diff = diff + 2
	count = count + 1
	
print( result )