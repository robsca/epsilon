# create a windows with tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from motors import move_motor

# create a window
window = tk.Tk()
window.title("Epsilon-bot")
window.geometry("800x800")

# create a button
testing_motors = ttk.Button(window, text="Testing Motors")
testing_motors.grid(column=0, row=0)

def create_label(text):
    label = ttk.Label(window, text=text)
    # at the right side of the window
    label.grid(column=0, row=14)
    # change color of label to light blue
    label.configure(background="light blue")

def motor_test():
    # create 10 buttons
    for i in range(12):
        button = ttk.Button(window, text=f"Button {i}")
        button.grid(column=0, row=i+1)
        # if button is clicked, print the text in the label
        button.configure(command=lambda text=f"Button {i}": create_label(text))
        
    
    # create a quit button
    quit_button = ttk.Button(window, text="Quit")
    quit_button.grid(column=0, row=13)
    quit_button.configure(command=window.destroy)

# create a function to run when the button is clicked
def click():
    print("Button clicked")
    window.bind("<Key>", pressed_key)
    # change color of window to light yellow
    window.configure(background="light yellow")
    # hide button
    testing_motors.grid_remove()
    motor_test()
    
def demonstration():
    print('demonstration mode')
    # ask the user for the coordinates
    x = 3
    y = 3
    z = 4
    from sol import inverse_kinematics
    s, e = inverse_kinematics(x, y, z)
    return s, e

# create function that returns the pressed_key
def pressed_key(event):
    pressed_key = event.char
    print(pressed_key)
    channels = [f'{i}' for i in range(16)]
    if pressed_key in channels:
        print("Channel: ", pressed_key)
    if pressed_key == 'a':
        s, e = demonstration()
        print(s, e)
        shoulder = 0
        elbow = 1
        move_motor(shoulder, s)
        move_motor(elbow, e)
        
    elif pressed_key == 'q':
        print("Quit")
        window.destroy()
    else:
        print("Invalid key: Not a channel")

    

def run():
    # run 
    testing_motors.configure(command=click)
    window.mainloop()

if __name__ == "__main__":
    run()