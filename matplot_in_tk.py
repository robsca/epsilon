import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#uncomment as needed to demonstrate 2d/3d plot
#subplot_kw = {'projection':'3d'}
subplot_kw = {}
fig, ax = plt.subplots(subplot_kw=subplot_kw)
if len(subplot_kw) > 0:
    ax.plot(range(100), np.random.rand(100), np.random.rand(100))
else:
    ax.plot(range(100), np.random.rand(100))

canvas = FigureCanvasTkAgg(fig, frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, frame)
toolbar.update()

root.mainloop()