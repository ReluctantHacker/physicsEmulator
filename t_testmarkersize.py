#coding=utf-8
import numpy as np
import plotext as plt
x = [1, 1, 2, 2]
y = [1, 2, 1, 2]
plt.xlim(-10, 10)
plt.ylim(-10, 10)


plt.scatter(x, y, marker = "big")
plt.plotsize(20, 20)
plt.colorless()
plt.show()
