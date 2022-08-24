import numpy as np
import matplotlib.pyplot as plt

np.loadtxt("data_points.txt")


x, f = np.loadtxt("data_points.txt",unpack = True)


X = np.atleast_2d(x).T
F = np.atleast_2d(f).T
p0 = x**0
p1 = x**1
p2 = x**2
 
p = np.column_stack(p0,p1,p2)