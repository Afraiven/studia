import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lorenz_system(state, t, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return dxdt, dydt, dzdt

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
    t_span = np.linspace(0, 25, int(25/h) + 1)
    solution = odeint(lorenz_system, initial_state, t_span, args=(sigma, rho, beta))
    x_vals, y_vals, z_vals = solution.T
    line1.set_data(y_vals, z_vals)
    return line1,

h_values = np.linspace(0.01, 0.5, 40)[::-1]
print(h_values)

ani = FuncAnimation(fig, update, frames=h_values, init_func=init, blit=True, repeat=False)
ani.save('lozenz_yz.gif', writer='pillow', fps=5, dpi=80)

plt.show()
