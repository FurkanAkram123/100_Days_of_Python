from turtle import Turtle 
franklin = Turtle()
franklin.shape("turtle")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "brown"]


screen = franklin.getscreen()

def draw_shape(Turtle, number_of_sides, side_length):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        Turtle.forward(side_length)
        Turtle.right(angle)

if __name__ == "__main__":
    for shape in range (3, 11):
        franklin.color(colors[shape - 3])
        draw_shape(franklin, shape, 100)
        
    screen.exitonclick()
    

