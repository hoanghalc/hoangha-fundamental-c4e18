from turtle import *
speed(-1)
shape("turtle")
canh = 50
for i in range(3, 7):
    if i % 2 == 0:
        color("red")
        for j in range(i):
            forward(100)
            left(360/i)
            canh += 10
    else:
        color("blue")
        for j in range(i):
            forward(100)
            left(360/i)
            canh += 10
mainloop()