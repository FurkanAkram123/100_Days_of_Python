from turtle import Turtle, Screen
import random
import tkinter as tk
import Screen

snake_body = []
movements = ["up", "down", "left", "right"]

if __name__ =="__main__":
    screen = Screen.create_screen()
    snake = Screen.create_snake()
    screen.listen()
    while True:
        snake.forward(10)
        if screen.onkey(key="up", fun=move_forward):
            
        if abs(snake.xcor())>400 or abs(snake.ycor())>300:
            messagebox = tk.messagebox.showinfo("Game Over!")
            break
    
    
    #snake.tracer(0)
    screen.exitonclick()
    
    


    
