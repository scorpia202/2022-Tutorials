import numpy as np
import matplotlib.pyplot as plt



x, f = np.loadtxt("data_points.txt",unpack = True)
data = np.column_stack((x,f))

X = np.atleast_2d(x).T
F = np.atleast_2d(f).T
p0 = x**0
p1 = x**1
p2 = x**2
 
P = np.column_stack((p0,p1,p2))

a = np.linalg.inv(P.T @ P) @ P.T @ F

fitted_trend = a[0] +a[1] * x+a[2] *x**2

smooth_x = np.linspace(0,3)
fitted_trend = a[0] +a[1] *smooth_x + a[2] *smooth_x**2

fig, ax = plt.subplots()
ax.scatter(x,f)
ax.plot(smooth_x, fitted_trend, 'r')

plt.show()
