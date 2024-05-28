import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Load the data
dane = pd.read_excel('COVID.xlsx')
dane = dane[1:]  # Remove the header row
dane = dane[:300]
dane.reset_index(drop=True, inplace=True)

# Calculate daily changes
dane['New_Confirmed'] = dane['Confirmed'].diff().fillna(dane['Confirmed'])
dane['New_Recovered'] = dane['Recovered'].diff().fillna(dane['Recovered'])
dane['New_Deaths'] = dane['Deaths'].diff().fillna(dane['Deaths'])

# Population size
N = 38_000_000

# Define the function for the infection rate
def infection_rate(t, beta, gamma, mu, I0):
    return I0 * np.exp((beta - gamma - mu) * t)

# Prepare the data for curve fitting
t = np.arange(len(dane))
I = dane['Confirmed'].values

# Normalize the infected data to prevent large values affecting the optimization
I_normalized = I / N

# Initial parameter guesses


initial_guess = [0.05, 0.023, 0.0004, I_normalized[0]]

# Fit the infection rate curve with constraints
try:
    params, _ = curve_fit(infection_rate, t, I_normalized, p0=initial_guess, bounds=(0, [1, 1, 1, 1]), maxfev=10000)
    beta, gamma, mu, I0 = params
    # Scale back the I0
    I0 *= N
except RuntimeError as e:
    print(f"Optimal parameters not found: {e}")
    beta, gamma, mu, I0 = [None]*4

# Print the estimated parameters
if all(param is not None for param in [beta, gamma, mu, I0]):
    print(f"Estimated beta: {beta}")
    print(f"Estimated gamma: {gamma}")
    print(f"Estimated mu: {mu}")
    print(f"Estimated I0: {I0}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(dane['Date'], dane['Confirmed'], 'r', alpha=0.7, linewidth=2, label='Infected')
plt.xlabel('Date')
plt.ylabel('Number of Infected People')
plt.legend()
plt.title('Infection Rate')
plt.show()
