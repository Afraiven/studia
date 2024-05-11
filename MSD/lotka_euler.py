# układ Lotki-Volterry metodą Eulera
import matplotlib.pyplot as plt

x0, last_x = 2, 2
y0, last_y = 1, 1
t = 0
#dt
h = 1
stop = 25
a = 1.2
b = 0.6
c = 0.3
d = 0.8
#F(xn, yn) = dy/dt = (a - b*y)*x
#F(xn, yn) = dx/dt = (c*x - d)*y

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
    
plt.figure(figsize=(10, 5))
plt.plot(t_wartosci, x_wartosci, label='Ofiary (x)', linestyle='-', color='red')
plt.plot(t_wartosci, y_wartosci, label='Drapieżnicy (y)', linestyle='-', color='blue')
plt.title(f'''Układ Lotki-Volterry zamodelowany przy pomocy metody Eulera (python)
          dt = {h}''')
plt.xlabel('t')
plt.ylabel('Populacje')
plt.legend()
plt.grid(True)
plt.show()