import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

def generate_values(h, stop=25, a=1.2, b=0.6, c=0.3, d=0.8, x=2, y=1, last_x=2, last_y=1, t=0):
    x_wartosci = [last_x]
    y_wartosci = [last_y]
    t_wartosci = [0]
    while t <= stop:
        x = last_x + h*(a - b*last_y)*last_x
        y = last_y + h*(c*last_x - d)*last_y
        x_wartosci.append(x)
        y_wartosci.append(y)
        last_x = x
        last_y = y
        t += h
        t_wartosci.append(t)
    return x_wartosci, y_wartosci, t_wartosci

fig, ax = plt.subplots()
line1, = ax.plot([], [], 'r-', label='Drapieżnicy')
line2, = ax.plot([], [], 'b-', label='Ofiary')
ax.set_xlim(0, 25)
ax.set_ylim(0.5, 20) 

ax.legend()
ax.set_title("Lotka-Volterra Metoda Eulera")
ax.set_xlabel("Czas")
ax.set_ylabel("Wielkości populacji")

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def update(h):
    x_values, y_values, t_values = generate_values(h)
    line1.set_data(t_values, x_values)
    line2.set_data(t_values, y_values)
    ax.set_title("Model Lotki-Volterry metodą Eulera dt = {0.5, 0.01} ")
    max_ = max(max(x_values), max(y_values))
    if max_ > 200:
        max_ = 200
    return line1, line2

h_values = [0.01*(i+1) for i in range(50)][::-1]
print(h_values)
ani = FuncAnimation(fig, update, frames=h_values, init_func=init, blit=True, repeat=False)


ani.save('lotka_volterra_dt_variation.gif', writer='pillow', fps=5, dpi=80)

plt.show()
