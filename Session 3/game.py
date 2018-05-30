from random import randint
a = randint(0,100)
count = 0
loop = True
while loop:
    if count >=7:
        print("het luot")
        loop = False
    else: 
        n = int(input("nhap n vao"))
        if n < a:   
            print("nho qua")
        elif n > a:
                
            print("nho qua")
        else:
            print("dung roi")
            loop = False
    count += 1    
      
