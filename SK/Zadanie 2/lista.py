import numpy as np
import random
from scipy import stats
from collections import Counter

import matplotlib.pyplot as plt

# random [0, 1)
def random_0_1():
    rand = 1
    while rand == 1:
        rand = random.random()
    return rand

def generate_rand_seq(n):
    seq = []
    for _ in range(n):
        seq.append(random_0_1())
    return seq

seq20 = generate_rand_seq(20)
print(seq20)
seq100 = generate_rand_seq(100)

def mean(seq):
    return sum(seq) / len(seq)

def median(seq):
    seq.sort()
    n = len(seq)
    if n % 2 == 0:
        return (seq[n//2 - 1] + seq[n//2]) / 2
    else:
        return seq[n//2]
    
def mode(seq):
    count = Counter(seq)
    mode_value, mode_count = count.most_common(1)[0]
    
    return mode_value

def variance(seq):
    n = len(seq)
    mean_seq = mean(seq)
    sum_sq = 0
    for i in range(n):
        sum_sq += (seq[i] - mean_seq)**2
    return sum_sq / (n-1)

def std_dev(seq):
    return variance(seq)**0.5

def skewness(seq):
    n = len(seq)
    mean_seq = mean(seq)
    std_dev_seq = std_dev(seq)
    sum_cub = 0
    for i in range(n):
        sum_cub += (seq[i] - mean_seq)**3
    return sum_cub / (n * std_dev_seq**3)

def kurtosis(seq):
    n = len(seq)
    mean_seq = mean(seq)
    std_dev_seq = std_dev(seq)
    sum_four = 0
    for i in range(n):
        sum_four += (seq[i] - mean_seq)**4
    return sum_four / (n * std_dev_seq**4)

def range_of(seq):
    return max(seq) - min(seq)

def print_stats(seq):
    print("Średnia:", mean(seq))
    print("Mediana:", median(seq))
    print("Dominanta:", mode(seq))
    print("Wariancja:", variance(seq))
    print("Odchylenie standardowe:", std_dev(seq))
    print("Skośność:", skewness(seq))
    print("Kurtoza:", kurtosis(seq))
    print("Rozstęp:", range_of(seq))

print("20 elementów:")
print_stats(seq20)

print("\n100 elementów:")
print_stats(seq100)

def plot_hist(seq):
    plt.title(f"Histogram dla {len(seq)} elementów")
    plt.xlabel("Wartość")
    plt.ylabel("Liczba wystąpień")
    plt.axhline(y=len(seq)/10, color='r', linestyle='-', label='Średnia liczba wystąpień dla U[0, 1)]')
    plt.hist(seq, bins=10)
    plt.show()

plot_hist(seq20)
plot_hist(seq100)

def density_function():
    x = np.linspace(0, 1, 100, endpoint=False) 
    y = stats.uniform.pdf(x, 0, 1)
    plt.plot(x, y)
    plt.title("Funkcja gęstości rozkładu równomiernego U[0, 1)")
    plt.xlabel("Wartość")
    plt.ylabel("Prawdopodobieństwo")
    plt.show()

density_function()
print()
def t_student_if_avg_is_half(seq):
    n = len(seq)
    mean_seq = mean(seq)
    std_dev_seq = std_dev(seq)
    t = (mean_seq - 0.5) / (std_dev_seq / n**0.5)
    p = 1 - stats.t.cdf(t, n-1)

    # hipoteza zerowa: średnia jest równa 0.5
    print("t:", t)
    print("p:", p)
    if p < 0.05:
        print("Odrzucamy hipotezę zerową")
    else:
        print("Nie ma podstaw do odrzucenia hipotezy zerowej")

print("20 elementów:")
t_student_if_avg_is_half(seq20)

print("\n100 elementów:")
t_student_if_avg_is_half(seq100)