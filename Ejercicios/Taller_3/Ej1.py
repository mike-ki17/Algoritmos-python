from turtle import *


begin_fill()
pensize(2)

for i in range(4):
    left(90)
    forward(150)

penup()
left(135)
forward(180)
left(90)
pendown()
forward(75)
for i in range(4):
    left(90)
    forward(150)

penup()
left(135)
forward(106)
pendown()

for i in range(8):
    forward(75)
    penup()
    forward(-75)
    left(45)
    pendown()

end_fill()
done()




