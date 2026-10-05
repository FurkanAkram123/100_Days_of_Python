import turtle, ASCII_Art

def main():
#create a turtle object
    franklin = turtle.Turtle()

#change the shape and color of the turtle
    franklin.shape("turtle")
    franklin.color("green")

# create a screen object from the turtle module
    screen = turtle.Screen()
    franklin.forward(100)

# print the width of the canvas
    print(screen.canvwidth)
    screen.exitonclick()


if __name__ == "__main__":
    print (ASCII_Art.logo)
    main()