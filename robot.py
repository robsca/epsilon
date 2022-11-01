'''
Create 3d Rendering in plotly
'''
import plotly.express as px
import pandas as pd
import math
class motor:    
    def __init__(self, name, x, y, z, type):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.type = type

class segment:
    def __init__(self, name, motor1, motor2, color):
        self.name = name
        self.motor1 = motor1
        self.motor2 = motor2
        self.color = color
        self.len = math.sqrt((motor1.x - motor2.x)**2 + (motor1.y - motor2.y)**2 + (motor1.z - motor2.z)**2)

class robot:
    def __init__(self, name, motors, segments):
        self.name = name
        self.motors = motors
        self.segments = segments
        self.angles = [0*len(motors)]

    # get all coords
    def get_coords(self):
        coords = []
        for motor in self.motors:
            coords.append([motor.x, motor.y, motor.z])
        return coords

    def get_angles(self):
        pass

    def show(self, cookie = None):
        coords = self.get_coords()
        df = pd.DataFrame(coords, columns=['x', 'y', 'z'])
        fig = px.scatter_3d(df, x='x', y='y', z='z' )
        # add markers and line
        for motor in self.motors:
            fig.add_trace(px.scatter_3d
                            (x=[motor.x], y=[motor.y], z=[motor.z], 
                            color_discrete_sequence=['black'],
                            ).data[0])
        for segment in self.segments:
            fig.add_trace(px.line_3d
                            (x=[segment.motor1.x, segment.motor2.x], y=[segment.motor1.y, segment.motor2.y], z=[segment.motor1.z, segment.motor2.z], 
                            color_discrete_sequence=[segment.color],
                            ).data[0])
        if cookie:
            # add trace
            x = cookie.x
            y = cookie.y
            fig.add_trace(px.line_3d
                            (x=[x[0], x[1]], y=[y[0], y[1]], z=[0, 0],
                            color_discrete_sequence=['red'],
                            ).data[0])
        fig.show()


        #fig.show()
        return fig

##########
# Testing

motor1 = motor("motor1", 0, 0, 0, "base")
motor2 = motor("motor2", 0, 0, 10, "body")
motor3 = motor("tip", 0, 0, 20, "tip")

segment1 = segment("segment1", motor1, motor2, "red")
segment2 = segment("segment2", motor2, motor3, "blue")

angle_segment1 = 0
angle_segment2 = 0

robot = robot("robot", [motor1, motor2, motor3], [segment1, segment2])
fig = robot.show()

# rendering
import streamlit as st
st.plotly_chart(fig)
