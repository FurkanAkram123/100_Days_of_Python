from turtle import Turtle


franklin = Turtle()
franklin.shape("turtle")


if __name__ == "__main__":
    #franklin.width(5) 
    franklin.speed("fastest")
    screen = franklin.getscreen()
    
    heading_change = 5
    for _ in range(int(360/heading_change)):
        franklin.setheading(franklin.heading() + heading_change)
        franklin.circle(100)
    
    franklin.getscreen().exitonclick()