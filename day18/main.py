import turtle as t
import random
import colorgram

colors = colorgram.extract('damien.jpg', 10)

tim = t.Turtle()
t.colormode(255)
tim.speed("slow")

print(colors)
rgb = colors[0].rgb
print(rgb.r)

def randomizeDot():
    rgb = colors[random.randint(0,9)].rgb
    return tim.dot(30, rgb)

def oneLine():
    for _ in range(9):
        randomizeDot()
        tim.fd(60)
        randomizeDot()

tim.penup()
tim.setpos(-270,-250)
for _ in range(5):
    oneLine()
    tim.left(90)
    tim.forward(60)
    tim.left(90)
    oneLine()
    tim.right(90)
    tim.forward(60)
    tim.right(90)





screen = t.Screen()
screen.exitonclick()