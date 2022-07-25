import numpy as numpy
from numpy import *
import pylab as pylab 
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import animation



fig=plt.figure()
ax=plt.axes(xlim=(0,100),ylim=(0,100))
line=ax.plot([],[],'ro')[0]

x=50
y=50
g=-9.8
vx=0.5
vy=0


def free_fall(i):
   # vy=vy+g*0.01
    global x
    global y
    global vx
    global vy
    vy = vy+g*0.01
    if y<0:
        vy=-vy
        vy=vy+g*0.01
        y=y+vy
        print(y,vy,i)
    else:
        y=y+vy
        print(y,vy,i)
    if x<0 or x>100:
        vx=-vx
        x=x+vx
    else: 
        x=x+vx
        
        
        
    line.set_data(x,y)
    return line,



anim=animation.FuncAnimation(fig,free_fall,interval=10)    
plt.show()     
