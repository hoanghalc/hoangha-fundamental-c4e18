import turtle, math

timmy = turtle.Turtle()
scr = turtle.Screen()

def regular(aturtle, length, sides, stmp = True):
    splits = 360.0 / sides
    for dist in range(sides):
        if stmp:
            aturtle.forward(length / 2)
            aturtle.stamp()
            aturtle.forward(length / 2)
        else:
            aturtle.forward(length)
        aturtle.left(splits)

# move timmy down and right (from his home position)
timmy.penup()
timmy.goto(-70, -70)
timmy.pendown()
# this is just to allow more room for the shapes
# which will be drawn above this position.

colours = ['red', 'green', 'blue', 'yellow', 'orange', 'pink', 'lightgreen']

for x in range(9, 3, -1):
    #print(x)    # 9,8,7,6,5,4
    timmy.fillcolor(colours[x - 3])
    timmy.begin_fill()
    regular(timmy, 30 + x*10, x)
    timmy.end_fill()
    timmy.penup()
    timmy.forward(5)        # why 5?
    timmy.pendown()

scr.mainloop()
