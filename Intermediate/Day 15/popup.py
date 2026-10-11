import tkinter as tk
from tkinter.messagebox import askyesno
from unittest import result

# Create the main hidden root window
root = tk.Tk()
root.withdraw() 

# Show the confirmation popup
def confirm_pick(user_pick):
    result = askyesno("Confirmation", f"Are you sure you want to order a {user_pick}?")

    if result:
        return True
    else:
        return False
