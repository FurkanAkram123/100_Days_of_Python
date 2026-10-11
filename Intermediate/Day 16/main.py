import turtle, ASCII_Art
from prettytable import PrettyTable

def draw_square():
    #create a turtle object
    franklin = turtle.Turtle()

#change the shape and color of the turtle
    franklin.shape("turtle")
    franklin.color("green")

# create a screen object from the turtle module

#make a square using the turtle object
    screen = turtle.Screen()
    franklin.forward(100)
    franklin.left(90)
    franklin.forward(100)
    franklin.left(90)
    franklin.forward(100)
    franklin.left(90)
    franklin.forward(100)

    #wait for the user to click on the screen before closing it
    screen.exitonclick()

def create_table():
    # create a table object
    table = PrettyTable()

    #add columns to the table
    table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"]) 
    table.add_column("Type", ["Electric", "Water", "Fire"])
    
    #align the table to the left
    table.align = "l"
    print (table)

def main():
    choice = input("Enter 'draw' to draw a square or 'table' to create a table: ")
    if choice.lower() == 'draw':
        draw_square()
    else:
        create_table()

if __name__ == "__main__":
    print (ASCII_Art.logo_pikachu)
    print (ASCII_Art.logo_turtle)
    main()