import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lorenz_system(h):
    t = 0
    sigma = 10.0
    rho = 28.0
    beta = 8/3
    x, y, z = 1.0, 1.0, 1.0
    #dt
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
    return x_wartosci, y_wartosci, z_wartosci
sigma = 10.0
rho = 28.0
beta = 8/3
initial_state = [1.0, 1.0, 1.0]

fig, ax = plt.subplots()
line1, = ax.plot([], [], 'r-', label='Lorenz', color='b')
ax.set_xlim(-30, 30)
ax.set_ylim(-1, 60)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()

def init():
    line1.set_data([], [])
    return line1,

def update(h):
    x_values, y_values, z_values = lorenz_system(h)
    line1.set_data(y_values, z_values)
    return line1,

h_values = np.linspace(0.01, 0.5, 40)[::-1]
print(h_values)

ani = FuncAnimation(fig, update, frames=h_values, init_func=init, blit=True, repeat=False)
ani.save('lozenz_euler_yz.gif', writer='pillow', fps=5, dpi=80)

plt.show()
