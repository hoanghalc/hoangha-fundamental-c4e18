n = int(input('nhap so vao'))

prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
       

if prime == True:
    print('{0} is a prime number'.format(n))
else:
    print("{0} not a prime".format(n))
            