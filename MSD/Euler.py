import matplotlib.pyplot as plt

# Ta metoda jest gorsza ze względu na ograniczenie RecursionError, lepsze są pętle / np.array
def euler_step(last_y, last_x, h, end, fn, dane=None):
    if dane is None:
        dane = [last_y]
    y =  last_y + h*fn(last_x, last_y)
    dane.append(y)
    if last_x >= end - h:
        return dane
    else:
        return euler_step(y, last_x+h, h, end, fn, dane)

h = 0.04

def wykres(y0, x0, h, finish, fn):
    wartosci_y = euler_step(y0, x0, h, finish, fn)
    wartosci_x = [i*h for i in range(len(wartosci_y))]

    plt.figure(figsize=(8, 4))
    plt.plot(wartosci_x, wartosci_y, marker='o', linestyle="-", color="b")
    plt.title('Metoda eulera')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

wykres(1, 2, 0.1, 25, lambda x, y: x-y)
