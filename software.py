import tkinter as tk
from Robot_ import robot, motors

# create a window
window = tk.Tk()
window.title('epsilon')
window.geometry('600x600')
# 1. Initialization
def button_for_initialization():
    # create a button for initialization
    initialization_ = tk.Button(window, text='Initialize', command=initialization)
    initialization_.grid(row = 0, column = 1)

def initialization():
    robot.initialize()
    print('Initialization completed')

# 2. Calibration
def button_for_calibration():
    # create a button for calibration
    calibration_ = tk.Button(window, text='Calibrate', command=calibration)
    calibration_.grid(row = 0,column = 2)

def calibration():
    # get all the values from the sliders
    def get_values():
        values = [slider.get() for slider in sliders]
        motors_to_modify = [[motor.name, value] for motor, value in zip(motors, values) if motor.angle != value]
        
        for motor in motors_to_modify:
            robot.move_motor(motor[0], motor[1])
            
    button = tk.Button(window, text='Move angles', command=get_values)
    button.grid(row = 10, column = 2)

# main_loop
# create a label for all the angles

    


sliders = []
for i, motor in enumerate(motors):
        label = tk.Label(window, text=motor.name)
        label.grid()
        # slider
        slider = tk.Scale(window, from_=motor.min, to=motor.max, orient=tk.HORIZONTAL)
        slider.grid(row=i+1, column=1)
        slider.set(motor.angle)
        sliders.append(slider)
        # button max
        def partial_max(motor):
            robot.move_motor(motor.name, motor.max)
            slider.set(motor.max)
        # create a button for min angle
        def partial_min(motor):
            robot.move_motor(motor.name, motor.min)
            slider.set(motor.min)
        # create a button for zero angle
        def partial_zero(motor):
            robot.move_motor(motor.name, 0)
            slider.set(0)

        #button max
        button_max = tk.Button(window, text='max', command=lambda: partial_max(motor))
        button_max.grid(row=i+1, column=2)
        # button min
        button_min = tk.Button(window, text='min', command=lambda: partial_min(motor))
        button_min.grid(row=i+1, column=3)
        # button mid
        button_mid = tk.Button(window, text='mid', command=lambda: partial_zero(motor))
        button_mid.grid(row=i+1, column=4)
        
# run the program
    
button_for_initialization()
button_for_calibration()
window.mainloop()
