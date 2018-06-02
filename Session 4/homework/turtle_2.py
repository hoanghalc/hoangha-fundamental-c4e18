from turtle import *
shape('turtle')
speed

canh = 10

for i in range(42):
    for j in range(4):
        forward(canh)
        left(90)   
    left(360/42)
    canh +=2

mainloop()