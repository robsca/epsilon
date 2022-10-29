import plotly.graph_objects as go
import numpy as np


# 6 axis robot
class Robot:
    def __init__(self, x, y, z, a, b, c):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.c = c

    def get_position(self):
        return [self.x, self.y, self.z, self.a, self.b, self.c]

    def set_position(self, x, y, z, a, b, c):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.c = c
    

def virtualization(robot):
    # plot the robot with plotly
    fig = go.Figure(data=[go.Scatter3d(x=[0, robot.x], y=[0, robot.y], z=[0, robot.z], mode='lines', line=dict(color='red', width=2))])
    fig.update_layout(scene = dict(
                        xaxis_title='X',
                        yaxis_title='Y',
                        zaxis_title='Z'),
                        width=700,

                        margin=dict(r=20, b=10, l=10, t=10))
    fig.show()


robot = Robot(0, 0, 0, 0, 0, 0)
virtualization(robot)
# change the position of the robot
robot.set_position(1, 1, 1, 0, 0, 0)
virtualization(robot)

