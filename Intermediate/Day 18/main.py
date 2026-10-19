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
        
def is_off_screen(turtle_x, turtle_y, screen_obj):
    
    # Get the current width and height of the window
    half_width = screen_obj.window_width() / 2
    half_height = screen_obj.window_height() / 2
       
    # Check if the position exceeds the boundaries
    if turtle_x > half_width or turtle_x < -half_width:
        return True
    if turtle_y > half_height or turtle_y < -half_height:
        return True
    
    return False
        
def draw_painting (Turtle, dot_size, space_between_dots, screen):
    
    #find the height and width of the screen
    window_height = screen.window_height()
    window_width = screen.window_width()
    start_x = -window_width/2 + 10
    start_y = -window_height/2 + 20
    
    # move to a starting position
    Turtle.penup()
    Turtle.goto(start_x,start_y)
    # Start at the bottom of the window
    while True:
        color_chosen = random.choice(color_list)
        Turtle.pendown()
        Turtle.dot(dot_size,color_chosen)
        Turtle.penup()
        if not is_off_screen((Turtle.xcor()+space_between_dots), Turtle.ycor(), screen):
            Turtle.forward(space_between_dots)
        else:
            Turtle.goto(start_x,Turtle.ycor()+space_between_dots)
            if is_off_screen(Turtle.xcor(), Turtle.ycor(), screen):
                Turtle.goto(0,0)
                break         

if __name__ == "__main__":
    #extract the color pallet from the painting
    extract_color_from_painting()
    
    #create a turtle object and describe parameters
    franklin = Turtle()
    franklin.shape("turtle") 
    franklin.speed("fastest")
    
    #draw a new painting
    screen = franklin.getscreen()
    screen.colormode(255)
    
    draw_painting(franklin, 10, 50, screen)
    # make sure screen doesnt close until clicked on
    screen.exitonclick()