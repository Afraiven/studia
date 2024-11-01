import numpy as np
import random
from scipy import stats
from collections import Counter
import matplotlib.pyplot as plt

random.seed(127)

def generate_normal(n):
    return [random.gauss(0, 1) for _ in range(n)]

seq20 = generate_normal(20)
seq100 = generate_normal(100)

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
    plt.title(f"Histogram gęstośxi dla {len(seq)} elementów")
    plt.xlabel("Wartość")
    plt.ylabel("Gęstość")
    x = np.linspace(min(seq), max(seq), 100)
    y = stats.norm.pdf(x, mean(seq), std_dev(seq))
    plt.plot(x, y, 'r')
    plt.hist(seq, bins=10, density=True)
    plt.show()

plot_hist(seq20)
plot_hist(seq100)

# qqplot
def qqplot(seq):
    stats.probplot(seq, plot=plt)
    plt.title(f"Q-Q plot dla {len(seq)} elementów")
    plt.show()

qqplot(seq20)
qqplot(seq100)

# boxplot
def boxplot(seq):
    plt.boxplot(seq)
    plt.title(f"Boxplot dla {len(seq)} elementów")
    plt.show()

boxplot(seq20)
boxplot(seq100)

def shapiro_wilk(seq):
    seq = sorted(seq)
    n = len(seq)
    mean_seq = np.mean(seq)
    std_dev_seq = np.std(seq, ddof=1) 
    stat, p_value = stats.shapiro(seq)

    print(f"Shapiro-Wilk W: {stat}, p-value: {p_value}")

print()
shapiro_wilk(seq20)
shapiro_wilk(seq100)

def student_test(seq):
    n = len(seq)
    mean_seq = mean(seq)
    std_dev_seq = std_dev(seq)
    t = mean_seq / (std_dev_seq / n**0.5)
    p_value = 2 * (1 - stats.t.cdf(abs(t), n-1))
    
    print(f"T-Student: {t}, p-value: {p_value}")

print()
student_test(seq20)
student_test(seq100)