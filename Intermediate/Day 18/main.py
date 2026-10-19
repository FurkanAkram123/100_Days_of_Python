import colorgram
from turtle import Turtle 
import random

colors = colorgram.extract('image.jpg',30)
color_list = []

def extract_color_from_painting():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        color_list.append(new_color)
        print (color_list)

def draw_painting (Turtle, number_of_dots, dot_size, space_between_dots):
    
    for _ in range(number_of_dots):
        color_chosen = random.choice(color_list)
        print (color_chosen)
        Turtle.dot(dot_size,color_chosen)
        Turtle.penup()
        Turtle.forward(space_between_dots)
        Turtle.pendown()

if __name__ == "__main__":
    #extract the color pallet from the painting
    extract_color_from_painting()
    
    #create a turtle object and describe parameters
    franklin = Turtle()
    franklin.shape("turtle"), franklin.speed("fastest")
    
    #draw a new painting
    screen = franklin.getscreen()
    screen.colormode(255)
    
    draw_painting(franklin, 10, 10, 50)
    # make sure screen doesnt close until clicked on
    screen.exitonclick()
    

