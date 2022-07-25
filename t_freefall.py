#coding=utf-8
import numpy as np
import plotext as plt


ini_y = 20
ini_x = 0
g = -9.8*0.01
ini_vx = 0
ini_vy = 0
plt.ylim(0,20)
plt.xlim(-10,10)
t = 1000
for dt in range(t):
    plt.cld()
    plt.clt()
    x = [0]
    y = [0]
    x[0] = ini_x + dt*ini_vx
    y[0] = ini_y + dt*(ini_vy+g*dt)
    plt.scatter(x, y, marker = "big")
    plt.plotsize(50,50)
    plt.colorless()
    plt.show()
