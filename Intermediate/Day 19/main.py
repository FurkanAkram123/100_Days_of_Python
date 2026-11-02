import turtle
import random
from tkinter import messagebox

screen = turtle.Screen()

number_of_turtles = 7 
turtles = []
color_list = ['red', 'blue', 'green', 'yellow', 'deepskyblue', 'limegreen', 'orange', 'magenta', 'purple', 'pink', 'brown', 'black']
turtle_colors = []

def create_turtles():
    #create turtle objects and give them a random color from the color list
    
    for x in range(number_of_turtles):
        new_turtle = turtle.Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        color_choice = random.choice(color_list)
            
        # Remove the chosen color to avoid duplicates
        color_list.remove(color_choice)  
        new_turtle.color(color_choice)
        
        turtles.append(new_turtle)
        turtle_colors.append(color_choice)
    
def start_race():
    # lineup the turtles on the screen
  for turtle in turtles:
    turtle.goto(x=-350, y=turtles.index(turtle)*50 - 200)  

def ready_set_go(bet):
   while True:
        for turtle in turtles:
            #move each turtle forward by a random distance
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)    
            
            # check if the turtle crossed the finsih line
            if turtle.xcor() > 350:
                
                winner = turtle.pencolor()
                if winner == bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You lose! The {winner} turtle is the winner!")
                return
            
if __name__ == "__main__":
    screen.setup(width=800, height=600)
    
    create_turtles()
    start_race()    
    
    try:
        bet = screen.textinput(title = "Welcome to the Turtle Race!", prompt = "Press pick your bet on which color will win: ")
        
        #put the bet in lower case
        bet = bet.lower()
        if bet not in turtle_colors:            
            raise ValueError("Invalid color")
        
        screen.listen()
        messagebox.showinfo("Notification", "press the space bar to start the race!")
        #press the space bar to start the race
        screen.onkey(key="space", fun=lambda: ready_set_go(bet))
        screen.exitonclick()
        
    except:
        messagebox.showerror("Error", "Closing the program because you did not enter a valid color. Please restart the program and try again.") 