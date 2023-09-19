import colorgram
import turtle as turtle_module
from turtle import Turtle, Screen
import random

turtle_module.colormode(255)
alt_colour_list = [(80, 177, 230), (130, 226, 97), (138, 48, 84), (54, 81, 159), (28, 120, 80), (118, 227, 186), (164, 48, 87), (25, 129, 176), (127, 195, 132)]
colour_list = [(80, 177, 230), (230, 226, 97), (238, 48, 84), (54, 81, 159), (228, 120, 80), (118, 227, 186), (164, 48, 87), (225, 129, 176), (127, 195, 132), (189, 20, 35), (244, 64, 48), (56, 46, 125), (190, 52, 37), (30, 165, 194), (70, 38, 48), (247, 163, 158), (63, 45, 36), (38, 211, 210), (234, 166, 180), (139, 213, 227), (101, 112, 168), (183, 181, 214), (250, 6, 21), (157, 33, 27), (169, 128, 80), (48, 50, 77), (69, 68, 44), (251, 9, 9)]
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(260)
tim.setheading(0)
def draw_damien_hirst(space, dot_size, number_rows , number_dots):
    for i in range(number_rows):
        for j in range(number_rows):
            tim.dot(dot_size, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            tim.forward(space)
        tim.backward(space * number_dots)
        tim.left(90)
        tim.forward(space)
        tim.right(90)
    tim.ht()

draw_damien_hirst(30, 20, 15, 15)
screen = Screen().exitonclick()
