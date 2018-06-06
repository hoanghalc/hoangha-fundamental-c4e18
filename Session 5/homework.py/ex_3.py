import math
b = int(input('How many B Bacterias are there? '))
t = int(input('How much time will we waits (minutes)? '))
r = b * 2 ** math.floor(t/2)
print ('After',t,'minutes(s) we would have',r,'B Bacterias')