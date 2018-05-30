from turtle import *
shape('turtle')
colors = ["red", "blue", "brown", "yellow", "grey"]
canh = 50
for i in range(0,5):
    color(colors[i])
    begin_fill()
    for i in range(2):
        forward(canh)
        right(90)
        forward(100)
        right(90)
    forward(canh)
    end_fill()
    

mainloop()

