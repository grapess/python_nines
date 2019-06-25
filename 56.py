def show( num ) :
	if num <= 10 :
		show( num + 1 )
		print(" [ " , num , " ] ",end='')		
		
show( 1 )