
import matplotlib.pyplot as plt


import numpy as np
import os
from numpy import linspace
def task1():
 fig, ax = plt.subplots()
 A = 1.34941
 x = linspace(-10, 10, 100)
 y = -0.0001*(abs(np.sin(x)*np.sin(A)*np.exp(abs(100-(((x**2+A**2)**0.5)/np.pi))))+1)**0.1

 ax.plot (x, y)

 plt.show()

 os.mkdir("results")
 f = open("results/task_01_4O-506C_Pripechenkov_6.txt", "w")
 print(' x \t f(x)', file=f)
 for i in range(100):
        print(x[i], '\t', y[i], file=f, end="\n")
 f.close

if os.path.exists('results'):
    os.remove('results/task_01_4O-506C_Pripechenkov_6.txt')
    os.rmdir("results")
    task1()
else:
    task1()