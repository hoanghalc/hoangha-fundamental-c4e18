from collections import defaultdict
d = defaultdict(list)
myList = [1,2,3,'a','b']
for x in myList:
   d[type(x)].append(x)

print (d[int])
print (d[str])