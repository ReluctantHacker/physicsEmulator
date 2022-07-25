import numpy as numpy
import pylab as pylab
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
#ax = plt.axes(xlim=(0,100), ylim(0,100))
ax=plt.axes(xlim=(-100,100), ylim=(-100,100))
Sun = ax.plot([],[],'bo')[0]
Earth = ax.plot([],[],'ro')[0]

#Def one dimensional gravitational acceleration formula
def lDGa(delta_x, delta_y, coordinate):
    if coordinate == 1:
        return -G*SunMass*delta_x/(delta_x**2 + delta_y**2)**(3/2)
    elif coordinate == 0:
        return -G*SunMass*delta_y/(delta_x**2 + delta_y**2)**(3/2)

#Def one dimensional gravitational force
def lDGf(delta_x, delta_y, coordinate):
    if coordinate == 1:
        return -G*SunMass*EarthMass*delta_x/(delta_x**2 + delta_y**2)**(3/2)
    elif coordinate == 0:
        return -G*SunMass*EarthMass*delta_y/(delta_x**2 + delta_y**2)**(3/2)

# Set physics constants
G = 0.1          # standard G is 0.1
SunMass = 1000     # standard Sun Mass is 100
EarthMass = 1     # standard earth Mass is 1

# Initial condition
ini_Sun_x = 0
ini_Sun_y = 0
ini_Sun_vx = 0.009   # initial x velocity 0.005 is standard, adjust this variable here
ini_Sun_vy = 0
#ini_Sun_ax = lDGf(ini_Sun_x, ini_Sun_y, 1)/SunMass 
#ini_Sun_ay = lDGf(ini_Sun_x, ini_sun_y, 0)/SunMass

ini_Earth_x = 0
ini_Earth_y = 40    # initial position of y is 40
ini_Earth_vx = -ini_Sun_vx*SunMass/EarthMass
ini_Earth_vy = 0

#ini_Earth_ax = lDGf(ini_Earth_x, ini_Earth_y, 1)/EarthMass
#ini_Earth_ay = lDGf(ini_Earth_x, ini_Earth_y, 0)/EarthMass

#Initial condition of accerelation
ini_delta_x = ini_Sun_x - ini_Earth_x
ini_delta_y = ini_Sun_y - ini_Earth_y
ini_Sun_ax = lDGf(ini_delta_x, ini_delta_y, 1)/SunMass
ini_Sun_ay = lDGf(ini_delta_x, ini_delta_y, 0)/SunMass

ini_Earth_ax = lDGf(-ini_delta_x, -ini_delta_y, 1)/EarthMass
ini_Earth_ay = lDGf(-ini_delta_x, -ini_delta_y, 0)/EarthMass


# Set the object position, velocity and acceleration variables, the size of the dots
Sun_x = ini_Sun_x
Sun_y = ini_Sun_y
Sun_vx = ini_Sun_vx
Sun_vy = ini_Sun_vy
Sun_ax = ini_Sun_ax
Sun_ay = ini_Sun_ay

Earth_x = ini_Earth_x
Earth_y = ini_Earth_y
Earth_vx = ini_Earth_vx
Earth_vy = ini_Earth_vy
Earth_ax = ini_Earth_ax
Earth_ay = ini_Earth_ay

# Set the time condition
tt = 1000
dt = 1 

constantV = 1
x = [Sun_x, Earth_x] 
y = [Sun_y, Earth_y]
# frame function
def gravitationalMotion(i):

    global x
    global y
    global Earth_ay
    global Earth_ax
    global Earth_vx
    global Earth_vy
    global Sun_ay
    global Sun_ax
    global Sun_vx
    global Sun_vy


    x[0] = x[0]+Sun_vx*dt
    y[0] = y[0]+Sun_vy*dt
    delta_x = x[0]-x[1]
    delta_y = y[0]-y[1]

    Sun_ay = lDGf(delta_x, delta_y, 0)/SunMass
    Sun_ax = lDGf(delta_x, delta_y, 1)/SunMass
    Sun_vx = Sun_vx + Sun_ax * dt
    Sun_vy = Sun_vy + Sun_ay * dt


    Earth_ay = lDGf(-delta_x, -delta_y, 0)/EarthMass
    Earth_ax = lDGf(-delta_x, -delta_y, 1)/EarthMass
    Earth_vx = Earth_vx + Earth_ax * dt
    Earth_vy = Earth_vy + Earth_ay * dt
    x[1] = x[1] + Earth_vx*dt
    y[1] = y[1] + Earth_vy*dt
    x[0] = x[0] + Sun_vx*dt
    y[0] = y[0] + Sun_vy*dt

    Sun.set_data(x[0], y[0])
    Sun.set_markersize(30)
    Earth.set_data(x[1], y[1])
    Earth.set_markersize(10)
    return Sun,

anim = animation.FuncAnimation(fig, gravitationalMotion, interval = 10)
plt.show()
