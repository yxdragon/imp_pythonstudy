import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

data = stream.read(CHUNK)


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 1024), ylim=(-20000, 20000))
line, = ax.plot([], [], lw=2) 
    
def animate(i):
    data = stream.read(CHUNK)
    y = np.frombuffer(data, dtype=np.int16)
    x = np.arange(len(y))
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)
                               
plt.show()
