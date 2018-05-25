for i in range(1,9):
    for j in range(1,9):
        if (i%2==1 and j%2==1) or (i%2==0 and j%2==0):
            print("1",end ="  ")
        else:
            print("0",end ="  ")
    print()