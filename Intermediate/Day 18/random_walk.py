from turtle import Turtle
import random

franklin = Turtle()
franklin.shape("turtle")

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

if __name__ == "__main__":
    franklin.width(5), franklin.speed("fastest")
    screen = franklin.getscreen()
    screen.colormode(255)
    for _ in range(50):
        franklin.color(random_color())
        franklin.forward(random.randint(10, 50))
        franklin.setheading(random.choice([0, 90, 180, 270]))     

    franklin.getscreen().exitonclick()