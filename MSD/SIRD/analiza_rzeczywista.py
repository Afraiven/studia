import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the data from the Excel file
dane = pd.read_excel('COVID.xlsx')[1:]
dane.reset_index(drop=True, inplace=True)

# Extract the data
confirmed = dane['Confirmed']
recovered = dane['Recovered']
deaths = dane['Deaths']
date = dane['Date']

# Total population (S + I + R + D = N)
n = 38_000_000

# Calculate the number of unaffected individuals (Susceptible)
unaffected = n - confirmed

# Calculate the number of currently infected individuals
currently_infected = confirmed - recovered - deaths

# Calculate derivatives
currently_infected_derivative = np.diff(currently_infected, prepend=currently_infected[0])
confirmed_derivative = np.diff(confirmed, prepend=confirmed[0])
recovered_derivative = np.diff(recovered, prepend=recovered[0])
deaths_derivative = np.diff(deaths, prepend=deaths[0])
unaffected_derivative = np.diff(unaffected, prepend=unaffected[0])

# Plot the actual state of the epidemic
plt.figure(figsize=(10, 6))
plt.plot(date, unaffected, 'g', alpha=0.7, linewidth=2, label='Susceptible')
plt.plot(date, confirmed, 'y', alpha=0.7, linewidth=2, label='Infected')
plt.plot(date, currently_infected, 'r', alpha=0.7, linewidth=2, label='Currently Infected')
plt.plot(date, recovered, 'b', alpha=0.7, linewidth=2, label='Recovered')
plt.plot(date, deaths, 'k', alpha=0.7, linewidth=2, label='Deceased')
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gcf().autofmt_xdate()
plt.xlabel('Data')
plt.ylabel('Liczba osób')
plt.legend()
plt.title('Rzeczywisty stan epidemii COVID-19 w Polsce 2020-2022')
plt.show()

# Plot the derivatives
plt.figure(figsize=(10, 6))
plt.plot(date, currently_infected_derivative, 'r', alpha=0.7, linewidth=2, label='Currently Infected - derivative')
plt.plot(date, recovered_derivative, 'b', alpha=0.7, linewidth=2, label='Recovered - derivative')
plt.plot(date, confirmed_derivative, 'b', alpha=0.7, linewidth=2, label='Infected - derivative')
plt.plot(date, deaths_derivative, 'k', alpha=0.7, linewidth=2, label='Deceased - derivative')
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gcf().autofmt_xdate()
plt.xlabel('Data')
plt.ylabel('Tempo zmian')
plt.legend()
plt.title('Tempo zmian stanu epidemii COVID-19 w Polsce 2020-2022')
plt.show()

# Plot the actual state of the epidemic
plt.figure(figsize=(10, 6))
plt.plot(date, currently_infected, 'r', alpha=0.7, linewidth=2, label='Currently Infected')
plt.plot(date, deaths, 'k', alpha=0.7, linewidth=2, label='Deceased')
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gcf().autofmt_xdate()
plt.xlabel('Data')
plt.ylabel('Liczba osób')
plt.legend()
plt.title('Rzeczywisty stan epidemii COVID-19 w Polsce 2020-2022')
plt.show()