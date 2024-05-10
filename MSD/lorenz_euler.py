import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sigma = 10.0
rho = 28.0
beta = 8/3

x, y, z = 1.0, 1.0, 1.0

#dt
h = 0.01
stop = 25

x_wartosci, y_wartosci, z_wartosci = [x], [y], [z]
t_wartosci = [0]
t = 0

while t <= stop:
    x_next = x + h * sigma * (y - x)
    y_next = y + h * (x * (rho - z) - y)
    z_next = z + h * (x * y - beta * z)
    
    x, y, z = x_next, y_next, z_next
    t += h

    x_wartosci.append(x)
    y_wartosci.append(y)
    z_wartosci.append(z)
    t_wartosci.append(t)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_wartosci, y_wartosci, z_wartosci, lw=0.5)
ax.set_title('Trajektoria układu Lorenza')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
