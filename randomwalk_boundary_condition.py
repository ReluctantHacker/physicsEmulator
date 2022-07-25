import numpy as numpy
from numpy import *
import pylab as pylab 
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import animation

fig=plt.figure()
ax=plt.axes(xlim=(-50,50),ylim=(-50,50))
line=ax.plot([],[],'ro')[0]

n=5000
x=[]
y=[]
for i in range(n):
    x.append(random()*10)
    y.append(random()*10)

def randomwalk(i):
    global x
    global y
    r=[]
    rs=[]
    
    
    
    for i in range(n):
        r.append(random()-0.5)
        rs.append(random()-0.5)
    x=array(x)+array(r)
    ry=sqrt(array(rs)**2)/rs*sqrt(0.5**2-array(r)**2)
    y=array(y)+ry   
    for a in range(n):
        if x[a]>50 or x[a]<-50:
            x[a]=x[a]-r[a]
    for a in range(n):
        if y[a]>50 or y[a]<-50:
            y[a]=y[a]-ry[a]             
            
            
    line.set_data(x,y)
    return line,
    
    
    
anim=animation.FuncAnimation(fig,randomwalk,interval=10)    
plt.show()
