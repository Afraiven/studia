import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lotka_volterra(y, t, a, b, c, d):
    x, y = y
    dxdt = x * (a - b * y)
    dydt = -y * (d - c * x)
    return [dxdt, dydt]

fig, ax = plt.subplots()
line1, = ax.plot([], [], 'r-', label='Drapieżnicy')
line2, = ax.plot([], [], 'b-', label='Ofiary')
ax.set_xlim(0, 25)
ax.set_ylim(0.5, 6) 

ax.legend()
ax.set_title("Lotka-Volterra funckja odeint")
ax.set_xlabel("Czas")
ax.set_ylabel("Wielkości populacji")

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

a = 1.2
b = 0.6
c = 0.3
d = 0.8

x0 = 2
y0 = 1
initial_conditions = [x0, y0]

dt = 3
kroki = int(25/dt) + 1
t = np.linspace(0, 25, kroki)
t_wartosci = np.linspace(0, 25, kroki)

def update(h): 
    kroki = int(25/h) + 1
    t = np.linspace(0, 25, kroki)
    solution = odeint(lotka_volterra, initial_conditions, t, args=(a, b, c, d))

    t_wartosci = np.linspace(0, 25, kroki)
    x_wartosci, y_wartosci = solution.T
    line1.set_data(t_wartosci, x_wartosci)
    line2.set_data(t_wartosci, y_wartosci)
    ax.set_title("Model Lotki-Volterry funkcją odeint dt = {0.5, 0.01} ")
    return line1, line2

h_values = [0.01*(i+1) for i in range(50)][::-1]
print(h_values)
ani = FuncAnimation(fig, update, frames=h_values, init_func=init, blit=True, repeat=False)


ani.save('lotka_volterra_scipy_dt_variation.gif', writer='pillow', fps=5, dpi=80)

plt.show()
