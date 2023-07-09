import random
from turtle import *
import colorgram
colors = colorgram.extract('hirst_paint.jpg', 30)
mycolors = []
for i in range(0, len(colors)):
    mycolors.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
print(mycolors)
colormode(255)
yinc = -200
t = Turtle()
t.penup()
t.setpos(-200,-200)
for i in range (0, 10):

    for j in range (0,10):
        t.penup()
        t.dot(20, random.choice(mycolors))
        #usecolor += 1
        t.fd(50)

    #t.home()

    yinc += 50
    t.setpos(-200,yinc)

mainloop()


