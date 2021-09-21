from turtle import Turtle
from random import randint
from scoreboard import Scoreboard
scoreboard = Scoreboard()
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(COLORS[randint(0,5)])
            new_car.penup()
            new_car.setpos(300, randint(-240,240))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT



        
