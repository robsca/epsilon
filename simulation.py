# create a plot of a triangle
import plotly.graph_objects as go
import numpy as np
import streamlit as st

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class joint:
    def __init__(self, p1, p2, len= 10):
        self.p1 = p1
        self.p2 = p2
        self.len = len

class robot:
    def __init__(self, points, joints):
        self.points = points
        self.tip = points[-1]
        self.joints = joints
        self.thetas = [0, 0, 0]
    
    def connect_joints(self):
        # connect the first joint
        self.joints[0].p2.x = self.joints[0].p1.x + self.joints[0].len * np.cos(self.thetas[0])
        self.joints[0].p2.y = self.joints[0].p1.y + self.joints[0].len * np.sin(self.thetas[0])
        # connect the second joint
        self.joints[1].p1.x = self.joints[0].p2.x
        self.joints[1].p1.y = self.joints[0].p2.y
        self.joints[1].p2.x = self.joints[1].p1.x + self.joints[1].len * np.cos(self.thetas[1])
        self.joints[1].p2.y = self.joints[1].p1.y + self.joints[1].len * np.sin(self.thetas[1])
        # connect the third joint
        self.joints[2].p1.x = self.joints[1].p2.x
        self.joints[2].p1.y = self.joints[1].p2.y
        self.joints[2].p2.x = self.joints[2].p1.x + self.joints[2].len * np.cos(self.thetas[2])
        self.joints[2].p2.y = self.joints[2].p1.y + self.joints[2].len * np.sin(self.thetas[2])
        # connect the tip
        self.tip.x = self.joints[2].p2.x
        self.tip.y = self.joints[2].p2.y
        return self.joints

    def plot_robot(self, cookie = None):
        # create a figure
        fig = go.Figure()
        # add the joints
        for j in self.joints:
            fig.add_trace(go.Scatter(x=[j.p1.x, j.p2.x], y=[j.p1.y, j.p2.y], mode="lines + markers"))
        # add the tip
        fig.add_trace(go.Scatter
        (x=[self.tip.x], y=[self.tip.y], mode="markers", marker=dict(size=10, color="purple")))
        if cookie:
            fig.add_trace(go.Scatter
            (x=[cookie.x], y=[cookie.y], mode="markers", marker=dict(size=10, color="red")))
        # add the axes name
        fig.update_layout(xaxis_title="x", yaxis_title="y")
        # range of the axes
        fig.update_xaxes(range=[-30, 30])
        fig.update_yaxes(range=[-30, 30])

        # show the figure
        st.plotly_chart(fig)

with st.sidebar.expander("Joint parameters"):
    # set the angle
    angle_1 = st.slider("Angle 1", -180, 180, 0)
    angle_2 = st.slider("Angle 2", -180, 180, 0)
    angle_3 = st.slider("Angle 3", -180, 180, 0)

# create three points
p1 = point(0, 0)
p2 = point(0, 10)
p3 = point(0, 20)
tip = point(0, 30)
# create three joints
j1 = joint(p1, p2, 10)
j2 = joint(p2, p3, 10)
j3 = joint(p3, tip,1)
# create a list of points and joints
points = [p1, p2, p3, tip]
joints = [j1, j2, j3]
# assign the angles
theta1 = np.radians(angle_1)
theta2 = np.radians(angle_2)
theta3 = np.radians(angle_3)
# ask the user to enter a x and y coordinate
x = st.number_input("Enter a x coordinate", -30, 30, 0)
y = st.number_input("Enter a y coordinate", -30, 30, 0)
cookie = point(x, y)

if __name__ == "__main__":
    # create a robot
    robot_ = robot(points, joints)
    robot_.thetas = [theta1, theta2, theta3]
    robot_.connect_joints()
    robot_.plot_robot(cookie)