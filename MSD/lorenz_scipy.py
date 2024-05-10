import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definicja funkcji Lorenza
def lorenz_system(state, t, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Parametry
sigma = 10.0
rho = 28.0
beta = 8/3

# Warunki początkowe
initial_state = [1.0, 1.0, 1.0]

# Wektor czasu
t = np.linspace(0, 50, 10000)  # Dłuższy czas dla bardziej szczegółowego obrazu dynamiki

# Rozwiązanie układu Lorenza
solution = odeint(lorenz_system, initial_state, t, args=(sigma, rho, beta))

# Rozpakowanie rozwiązania
x, y, z = solution.T

# Tworzenie wykresu 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5)
ax.set_title('Trajektoria układu Lorenza')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
