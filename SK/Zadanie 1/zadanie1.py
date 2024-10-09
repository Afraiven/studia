import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def simulate_shot():
    x = np.random.uniform(0, 40)
    y = np.random.uniform(0, 40)
    distance = np.sqrt((x - 20) ** 2 + (y - 20) ** 2)
    
    if distance <= 2:
        return x, y, 10
    elif distance <= 4:
        return x, y, 9
    elif distance <= 6:
        return x, y, 8
    elif distance <= 8:
        return x, y, 7
    elif distance <= 10:
        return x, y, 6
    elif distance <= 12:
        return x, y, 5
    elif distance <= 14:
        return x, y, 4
    elif distance <= 16:
        return x, y, 3
    elif distance <= 18:
        return x, y, 2
    elif distance <= 20:
        return x, y, 1
    else:
        return x, y, 0

def simulate_archer(shots):
    results = []
    coordinates = []
    for _ in range(shots):
        x, y, score = simulate_shot()
        results.append(score)
        coordinates.append((x, y))
    mean_score = np.mean(results)
    std_dev = np.std(results)
    return results, coordinates, mean_score, std_dev

def plot_shots(coordinates, shots):
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 40)
    
    for radius in range(2, 22, 2):
        circle = plt.Circle((20, 20), radius, color='black', fill=False)
        ax.add_artist(circle)
    
    x_coords, y_coords = zip(*coordinates)
    ax.scatter(x_coords, y_coords, color='red')
    
    plt.title(f'Łucznik strzelił {shots} razy')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def chi_squared_test(results, i, a=0.05):
    df = len(results) - 1
    critical_value = stats.chi2.ppf(1 - a, df)

    actual_value, actual_values = calc_value_area_of_full_circle()
    observed = []
    for j in range(11):
        observed.append(results.count(j))
    observed = np.array(observed)
    mean = 3.0237 # Średnia wartość dla nieskończonej liczby strzałów
    infinte = np.array([mean * i/10 for _ in actual_values])
    chi_squared = np.sum((observed - infinte) ** 2 / infinte)
    
    p_value = 1 - stats.chi2.cdf(chi_squared, df)
    
    if chi_squared < critical_value:
        print(f"Nie odrzucamy hipotezy zerowej dla poziomu istotności {a}\n"
              f"Wartość statystyki: {chi_squared}\n"
              f"Wartość krytyczna: {critical_value}\n"
              f"p-value: {p_value}")
    else:
        print(f"Odrzucamy hipotezę zerową dla poziomu istotności {a}\n"
              f"Wartość statystyki: {chi_squared}\n"
              f"Wartość krytyczna: {critical_value}\n"
              f"p-value: {p_value}")
        
def calc_value_area_of_full_circle():
    suma = 0
    total_area_square = 40 ** 2
    total_area_circle = np.pi * 20 ** 2

    actual_values = []

    for i in range(10):
        if i == 0:
            area = np.pi * (2 * (i+1)) ** 2
            points = 10
        else:
            area = np.pi * (2 * (i+1)) ** 2 - np.pi * (2 * i) ** 2
            points = 10 - i

        suma += area * points
        actual_values.append((area * points) / total_area_square)

    outside_area = total_area_square - total_area_circle
    actual_values.append((outside_area * 0) / total_area_square)
    suma += outside_area * 0
    actual_value = suma / total_area_square

    return actual_value, actual_values

def main():
    shot_counts = [10, 100, 1000]
    means = []
    for shots in shot_counts:
        results, coordinates, mean_score, std_dev = simulate_archer(shots)
        means.append(mean_score)
        print("*" * 50)
        print(f"Strzały: {shots}, Średnia: {mean_score}, Odchylenie: {std_dev}")
        print(f"Wnik testu chi kwadrat:")
        chi_squared_test(results, shots)
        plt.hist(results, bins=range(12), edgecolor='black', align='left')
        plt.title(f'Histogram {shots} strzałów')
        plt.xlabel('Wynik')
        plt.ylabel('Częstotliwość')
        plt.show()
        plot_shots(coordinates, shots)
    
    return means

means = main()
actual_value, _ = calc_value_area_of_full_circle()
print("Średnia wartość rzeczywista gdy n-> inf: ", actual_value)
shots = [10, 100, 1000, 10_000, 100_000]
plt.clf()  
plt.close()  
plt.plot(shots, means, label='Średnia wartość', marker='o')
plt.axhline(y=actual_value, color='r', linestyle='-', label='Wartość rzeczywista')

plt.xscale('log')

plt.legend()
plt.title('Średnia wartość dla różnej liczby strzałów')
plt.xlabel('Liczba strzałów')
plt.ylabel('Średnia wartość')

plt.show()

