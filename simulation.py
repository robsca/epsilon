# create a plot of a triangle
import plotly.graph_objects as go
import numpy as np
import streamlit as st

# create points
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# create the joint  
class joint:
    def __init__(self, p1, p2, len= 10):
        self.p1 = p1
        self.p2 = p2
        self.len = len
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

joints = [j1, j2, j3]

theta1 = np.radians(angle_1)
theta2 = np.radians(angle_2)
theta3 = np.radians(angle_3)

# connect the joints
def connect_joints(joints):
    # connect the first joint
    joints[0].p2.x = joints[0].p1.x + joints[0].len * np.cos(theta1)
    joints[0].p2.y = joints[0].p1.y + joints[0].len * np.sin(theta1)
    # connect the second joint
    joints[1].p1.x = joints[0].p2.x
    joints[1].p1.y = joints[0].p2.y
    joints[1].p2.x = joints[1].p1.x + joints[1].len * np.cos(theta2)
    joints[1].p2.y = joints[1].p1.y + joints[1].len * np.sin(theta2)
    # connect the third joint
    joints[2].p1.x = joints[1].p2.x
    joints[2].p1.y = joints[1].p2.y
    joints[2].p2.x = joints[2].p1.x + joints[2].len * np.cos(theta3)
    joints[2].p2.y = joints[2].p1.y + joints[2].len * np.sin(theta3)
    # connect the tip
    tip.x = joints[2].p2.x
    tip.y = joints[2].p2.y
    return joints

def plot_robot(joints):
    # create a figure
    fig = go.Figure()
    # add the joints
    for j in joints:
        fig.add_trace(go.Scatter(x=[j.p1.x, j.p2.x], y=[j.p1.y, j.p2.y], mode="lines + markers"))
    # add the tip
    fig.add_trace(go.Scatter
    (x=[tip.x], y=[tip.y], mode="markers", marker=dict(size=10, color="purple")))
    # add the axes name
    fig.update_layout(xaxis_title="x", yaxis_title="y")
    # range of the axes
    fig.update_xaxes(range=[-30, 30])
    fig.update_yaxes(range=[-30, 30])

    # show the figure
    st.plotly_chart(fig)

# main function
def main():
    joints_ = connect_joints(joints)
    plot_robot(joints_)

if __name__ == "__main__":
    main()


