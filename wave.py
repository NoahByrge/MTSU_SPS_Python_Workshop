import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

wavelength = 0.25
period = 100
wave_number = 2 * np.pi / wavelength
angular_frequency = 2 * np.pi / period

fig = plt.figure()

ax = plt.axes(xlim = (0, 1), ylim = (-1.25, 1.25))

line, = ax.plot([], [], lw = 3)

def init():
    line.set_data([], [])
    return line,

def animate(t):
    x = np.linspace(0, 1, 100)
    
    y = np.sin(wave_number * x - angular_frequency * t)
    line.set_data(x, y)
    
    return line,

anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True)

anim.save('wave.mp4', writer = 'ffmpeg', fps = 30)