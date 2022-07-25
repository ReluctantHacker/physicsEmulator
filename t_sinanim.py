#coding=utf-8
import plotext as plt
import numpy as np

x = []
for i in range(100):
    x.append(i)


t = 1000
y = []
plt.ylim(-1.5, 1.5)
wave_speed = 2
for dt in range(t):
    plt.cld()
    plt.clt()
    y = []
    for i in range(100):
        y.append(np.sin((i+wave_speed*dt)/10))

    plt.scatter(x, y, marker = "dot")
    plt.colorless()
    plt.show()
