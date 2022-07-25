import numpy as np
import math
import plotext as plt

# Def one dimensional gravitational forumula
def lDGa(x, y, coordinate):
    if coordinate == 1:
        return -G*SunMass*x/(x**2 + y**2)**(3/2)
    elif coordinate == 0:
        return -G*SunMass*y/(x**2 + y**2)**(3/2)



# Set physics constants
G = 0.1
SunMass = 100
EarthMass = 1


# Initial condition
ini_Sun_x = 0
ini_Sun_y = 0
ini_Sun_vx = 0
ini_Sun_vy = 0
ini_Sun_ax = 0
ini_Sun_ay = 0

ini_Earth_x = 0
ini_Earth_y = 40
ini_Earth_vx = 0.5
ini_Earth_vy = 0
ini_Earth_ax = lDGa(ini_Earth_x, ini_Earth_y, 1)
ini_Earth_ay = lDGa(ini_Earth_x, ini_Earth_y, 0)


# Set the object position, velocity and acceleration variables, the size of the dots
Sun_x = [ini_Sun_x, ini_Sun_x, ini_Sun_x + 0.5, ini_Sun_x + 0.5]
Sun_y = [ini_Sun_y, ini_Sun_y+0.5, ini_Sun_y, ini_Sun_y+0.5]
Sun_vx = ini_Sun_vx
Sun_vy = ini_Sun_vy
Sun_ax = ini_Sun_ax
Sun_ay = ini_Sun_ay

Earth_x = [ini_Earth_x]
Earth_y = [ini_Earth_y]
Earth_vx = ini_Earth_vx
Earth_vy = ini_Earth_vy
Earth_ax = ini_Earth_ax
Earth_ay = ini_Earth_ay

# Set the plot
plt.ylim(-50,50)
plt.xlim(-50,50)

# Set the time condition
tt = 1000
dt = 1

# Plot the animation
for t in range(tt):
    plt.cld()
    #Sun_ay = lDGa(Sun_x[0], Sun_y[0], 0)
    #Sun_ax = lDGa(Sun_x[0], Sun_y[0], 1)
    #Sun_vx = Sun_vx + Sun_ax*dt
    #Sun_vy = Sun_vy + Sun_ay*dt
    Sun_x[:] = map(lambda x: x+Sun_vx*dt, Sun_x)
    Sun_y[:] = map(lambda y: y+Sun_vy*dt, Sun_y)

    Earth_ay = lDGa(Earth_x[0], Earth_y[0], 0)
    Earth_ax = lDGa(Earth_x[0], Earth_y[0], 1)
    Earth_vx = Earth_vx + Earth_ax*dt
    Earth_vy = Earth_vy + Earth_ay*dt
    Earth_x[:] = map(lambda x: x+Earth_vx*dt, Earth_x)
    Earth_y[:] = map(lambda y: y+Earth_vy*dt, Earth_y)

    plt.scatter(Sun_x, Sun_y, marker = "big")
    plt.scatter(Earth_x, Earth_y, marker = "dot")
    plt.plotsize(100,50)
    plt.colorless()
    plt.show()
