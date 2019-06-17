x1=int(input("value of x1:"))
x2=int(input("value of x2:"))
x3=int(input("value of x3:"))
y1=int(input("value of y1:"))
y2=int(input("value of y2:"))
y3=int(input("value of y3:"))
res1 = (y3-y2)/(x3-x2)
res2 = (y2-y1)/(x2-x1)
print(res1 , res2 )
if res1 == res2 :
	print("points lie on straight line")
else:
	print("points are not lie on straight line")