def sum_one():
	n1 = 43
	n2 = 432
	ans = n1 + n2
	print( " Sum : " , ans )
	
def sum_two( n1 , n2 ):
	ans = n1 + n2
	print( " Sum : " , ans )
	
def sum_three( n1 , n2 ):
	ans = n1 + n2
	return ans
	
if __name__ == "__main__":
	sum_one()
	sum_two( 43 ,23 )
	sum_two( 453,65 )
	value = sum_three( 543 ,23 )
	print(" Sum of Given Number : " , value )
	print(" Sum of Number : " , sum_three( 11 , 33 ))