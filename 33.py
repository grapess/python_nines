total = 21

while True:
	print(" Total Matchstick Available : " , total )
	print(" User can Pick 1 , 2 , 3 , 4 Matchstick ")
	pick = int( input(" Enter Number of Matchstick you want to Pick : "))
	if pick >= 1 and pick <= 4 :
		computer_pick = 5 - pick
		print(" Computer Pick : " , computer_pick , " matchstick")
		total -= 5
	else:
		print(" Invalid Number of Matchstick Given. So Try Again ")
	if total == 1 :
		break
		
print(" There are only 1 matchstick remaining. User have to pick it ")
print(" So Computer Wins!!! ")