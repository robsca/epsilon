import plotly.graph_objects as go
import pandas as pd




# create a dataframe with the points
coords = [[0, 0, 10], [0, 0, 20], [0, 0, 30], [0, 0, 40], [0, 0, 50], [0, 0, 60]]
df = pd.DataFrame(coords, columns=['x', 'y', 'z'])

def virtualization(df):
    # create a figure
    fig = go.Figure()
    # add a scatter3d trace
    fig.add_trace(go.Scatter3d(x=df['x'], y=df['y'], z=df['z'], mode='lines+markers', line=dict(color='red', width=2)))

    # update the layout
    fig.update_layout(scene = dict(
                        xaxis_title='X',
                        yaxis_title='Y',
                        zaxis_title='Z'),
                        width=700,
                        margin=dict(r=20, b=10, l=10, t=10))
    fig.show()
