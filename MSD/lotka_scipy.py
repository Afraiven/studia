import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definicja funkcji modelu Lotki-Volterry
def lotka_volterra(y, t, a, b, c, d):
    x, y = y
    dxdt = x * (a - b * y)
    dydt = -y * (d - c * x)
    return [dxdt, dydt]

# Parametry modelu
a = 1.2
b = 0.6
c = 0.3
d = 0.8

# Warunki początkowe
x0 = 2
y0 = 1
initial_conditions = [x0, y0]

# Wektor czasu
t = np.linspace(0, 25, 400)

# Rozwiązanie równań różniczkowych
solution = odeint(lotka_volterra, initial_conditions, t, args=(a, b, c, d))

# Rozpakowanie rozwiązania
x, y = solution.T

# Tworzenie wykresu
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Ofiary (x)')
plt.plot(t, y, label='Drapieżnicy (y)')
plt.title('Dynamika populacji w modelu Lotki-Volterry')
plt.xlabel('Czas')
plt.ylabel('Populacja')
plt.legend()
plt.grid(True)
plt.show()
