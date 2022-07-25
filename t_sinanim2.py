#coding=utf-8
import plotext as plt
import numpy as np
import os

x = []
for i in range(100):
    x.append(i)


t = 1000
y = []
plt.ylim(-1.5, 1.5)
wave_speed = 1 
for dt in range(t):
    plt.cld()
    #plt.clt()
    #plt.clf()
    y = []
    for i in range(100):
        y.append(np.sin((i+wave_speed*dt)/10))

    plt.scatter(x, y, marker = "dot")
    plt.colorless()
    plt.show()
