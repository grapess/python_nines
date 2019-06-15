year = int( input(" Enter Any Year : "))

# Normal Year : 365 Days = 52 Weeks + 1 day
# Leap Year : 366 Days  = 52 Weeks + 2 day
total_days = ( year - 1 ) * 365
total_days += ( year - 1 ) // 4
total_days -= ( year - 1 ) // 100
total_days += ( year - 1 ) // 400

rem = total_days % 7

result = "On 1st January, " + str(year) + " has "

if rem == 0 :
	result += "Monday"
else:
	if rem == 1 :
		result += "Tuesday"
	else:
		if rem == 2:
			result += "Wednesday"
		else:
			if rem == 3:
				result += "Thursday"
			else:
				if rem == 4:
					result += "Friday"
				else:
					if rem == 5:
						result += "Saturday"
					else:
						result += "Sunday"

result += "."

print( result )