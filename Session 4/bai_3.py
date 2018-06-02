print("guess my number from 0-100")

low = 0
high = 100
mid = (low + high)/2

print(''''
c is correct
l is lager 
s is smaller
''')

while True:
    ans = input('is {0} your number?'.format(mid)).lower() # dùng lower() và upper() để in thường hoặc in hoa tất cả ký tự
    if ans == 's':
        low = mid
        mid = (low + high)//2
    elif ans == 'l':
        high = mid
        mid = (low + high)//2   
    elif ans == 'c':
        print('dung roi')
        break
    else:
        print('dung co ma troll tao')

    
        