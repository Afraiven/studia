import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import time
sigma = 10.0
rho = 28.0
beta = 8/3

x, y, z = 1.0, 1.0, 1.0

#dt
h = 0.001
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
ax.plot(x_wartosci, y_wartosci, z_wartosci, lw=1)
ax.set_title('Układ Lorenza zamodelowany przy pomocy metody Eulera (python)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# plt.figure(figsize=(7, 6))
# plt.plot(x_wartosci, y_wartosci, linestyle='-', color='r')
# plt.title(f'''Układ Lorenza zamodelowany przy pomocy metody Eulera (python)
#           dt = {h}''')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(7, 6))
# plt.plot(x_wartosci, z_wartosci, linestyle='-', color='g')
# plt.title(f'''Układ Lorenza zamodelowany przy pomocy metody Eulera (python)
#           dt = {h}''')
# plt.xlabel('X')
# plt.ylabel('Z')
# plt.legend()
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(7, 6))
# plt.plot(y_wartosci, z_wartosci, linestyle='-', color='b')
# plt.title(f'''Układ Lorenza zamodelowany przy pomocy metody Eulera (python)
#           dt = {h}''')
# plt.xlabel('Y')
# plt.ylabel('Z')
# plt.legend()
# plt.grid(True)
# plt.show()