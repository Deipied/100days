from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

for i in range(3, 12):
    n = 180 - (180(i-2))/3
    for _ in range(12):
        tim.forward(4 + 2 * i)
        tim.left(n)
    
    



screen.listen()
screen.onkey(clear, "c")
screen.exitonclick()