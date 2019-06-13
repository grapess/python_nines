from math import *

num = int(input(" Enter Any Number : "))

result = sqrt( num )

print( " Square Root : " , result )

ans = floor( result )

print( " Floor : " , ans )

ans = ceil( result )

print( " Ceil : " , ans )

ans = log10( num )

print( " Log 10 : " , ans )

ans = ceil(log10( num ))

print( " Total Digit of Given Number : " , ans )