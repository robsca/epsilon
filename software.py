
'''
this software takes 6 inputs and return the sum of the inputs
'''
from robot import robot
import tkinter as tk

# create a window
window = tk.Tk()
window.title('epsilon')
window.geometry('500x500')

# create a label for all the angles
label = tk.Label(window, text='Enter the angles')
label.pack()

from 
# create a entry for the channel
entry1 = tk.Entry(window)
entry1.pack()

label1 = tk.Label(window, text='Angle 1')
label1.pack()
# then the slider
slider1 = tk.Scale(window, from_=0, to=180, orient=tk.HORIZONTAL)
slider1.pack()


# create a function to sum the inputs
def sum():
    # get the values from the sliders
    value1 = slider1.get()
    value2 = slider2.get()
    value3 = slider3.get()
    value4 = slider4.get()
    value5 = slider5.get()
    value6 = slider6.get()
    # sum the values
    sum = value1 + value2 + value3 + value4 + value5 + value6
    # create a label to show the sum
    label_sum = tk.Label(window, text='The sum is: {}'.format(sum))
    label_sum.pack()

# bind the button to the function
button.bind('<Button-1>', lambda event: sum())

# run the window
window.mainloop()
