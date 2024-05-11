import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definicja funkcji modelu Lotki-Volterry
def lotka_volterra(y, t, a, b, c, d):
    x, y = y
    dxdt = x * (a - b * y)
    dydt = -y * (d - c * x)
    return [dxdt, dydt]

a = 1.2
b = 0.6
c = 0.3
d = 0.8

x0 = 2
y0 = 1
initial_conditions = [x0, y0]

dt = 0.01
kroki = int(25/dt) + 1
t = np.linspace(0, 25, kroki)

solution = odeint(lotka_volterra, initial_conditions, t, args=(a, b, c, d))

x, y = solution.T



plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Ofiary (x)', color="r")
plt.plot(t, y, label='Drapieżnicy (y)', color="b")
plt.title(f'''Układ Lotki-Volterry zamodelowany przy pomocy funckji odeint (scipy)
          dt = {dt}''')
plt.xlabel('t')
plt.ylabel('Populacje')
plt.legend()
plt.grid(True)
plt.show()
