from turtle import Turtle, Screen
import random
import numpy as np
timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)
timmy.speed("fastest")
sides = 3

while sides <= 5:
  number = 360 / sides
  random_color = tuple(np.random.choice(range(256), size=3))
  for _ in range(sides):
    timmy.color(random_color)
    timmy.forward(100)
    timmy.right(number)
  sides +=1

timmy.circle(150)
timmy.setheading(45)

timmy.setheading(90)
timmy.circle(70)
screen.exitonclick()
