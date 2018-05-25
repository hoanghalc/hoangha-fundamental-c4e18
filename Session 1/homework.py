EX1: Calculate area of a circle
import math 
from math import pi 
rad = float(input("Radius of the circle is:"))
s = (rad**2) * pi
print("The area of the circle is:", s)  
 
EX2: converts Celsius (0C) into Fahrenheit (0F) 
cel = float(input("enter the temperature in celsius"))
fah = (cel * 1.8) + 32
print("Temperature is", fah, "F") 

EX3: Turtle exercise
from turtle import *
speed(-1)
shape("turtle")
color("green")
fillcolor("yellow")
begin_fill()

draw square
forward(100)
left(90) 
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)


draw equilateral triangle
forward(100)
left(120)
forward(100)
left(120)
forward(100)

draw circle
circle(100)

draw Multi-circles
for i in range(300):
    circle(100)
    left(30)


end_fill()
mainloop()
