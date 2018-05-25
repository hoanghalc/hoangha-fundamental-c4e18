canh = int(input("Nhap so canh cua da giac"))
from turtle import *
speed(-1)
shape("turtle")
color("green")
fillcolor("cyan")
begin_fill()
#draw square

for i in range(canh):
    forward(100)
    right(360/canh) 
    # forward(100)
    # left(90)
    # forward(100)
    # left(90)
    # forward(100)
    # left(90)
    

end_fill()

mainloop()
