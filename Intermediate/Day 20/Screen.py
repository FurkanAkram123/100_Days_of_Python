from turtle import Turtle, Screen

def create_screen():
    screen = Screen()

    #screen setup
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    
    return screen

#create the intial snake body

def create_snake():
    snake = Turtle(shape="square")
    snake.color("white")
    snake.turtlesize(stretch_wid=0.5, stretch_len=1)
    snake.penup()
    return snake
