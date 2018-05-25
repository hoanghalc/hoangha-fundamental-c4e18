n = int(input("nhap n vao"))
for i in range(1,n+1):
    print( i, end=" ")
    for j in range(1,n+1):
        print("{:2d}".format(i*j), end=" ")
    print()
