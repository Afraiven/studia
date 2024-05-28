import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# S (Susceptible) - osoby podatne na zakażenie.
# I (Infected) - osoby zakażone.
# R (Recovered) - osoby wyzdrowiałe.
# D (Deceased) - osoby zmarłe.

# S + I + R + D = N
# N = stała populacyjna (bez zmian demograficznych)

beta_poczatek = 0.055
beta_koniec = 0.055
gamma = 0.009
mi = 0.0002

#beta = 0.000000000679
#gamma = 0.00132033544
#mi = 0.0000584
dane = pd.read_excel('COVID.xlsx')[1:]
date = dane['Date']

S0 = 38_000_000
I0 = 1
R0 = 0
D0 = 0
y0 = [S0, I0, R0, D0]
N = sum(y0)

dt = 1  
dni = 787
t = np.arange(0, dni, dt)

def beta_linear(t, t_max, beta_start, beta_end):
    return beta_start + (beta_end - beta_start) * t / t_max

def deriv(y, t, N, gamma, mi, t_max, beta_start, beta_end):
    S, I, R, D = y
    beta_t = beta_linear(t, t_max, beta_start, beta_end)
    dSdt = -beta_t * S * I / N
    dIdt = beta_t * S * I / N - gamma * I - mi * I
    dRdt = gamma * I
    dDdt = mi * I
    return dSdt, dIdt, dRdt, dDdt

solution = odeint(deriv, y0, t, args=(N, gamma, mi, dni, beta_poczatek, beta_koniec))
S, I, R, D = solution.T

S_derivative = np.diff(S, prepend=S[0]) / dt
I_derivative = np.diff(I, prepend=I[0]) / dt
R_derivative = np.diff(R, prepend=R[0]) / dt
D_derivative = np.diff(D, prepend=D[0]) / dt

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(date, S[:len(date)], 'g', alpha=0.7, linewidth=2, label='Susceptible')
ax.plot(date, I[:len(date)], 'r', alpha=0.7, linewidth=2, label='Infected')
ax.plot(date, R[:len(date)], 'b', alpha=0.7, linewidth=2, label='Recovered')
ax.plot(date, D[:len(date)], 'k', alpha=0.7, linewidth=2, label='Deceased')
ax.set_xlabel('Data')
ax.set_ylabel('Liczba osób')
ax.legend()
ax.set_title('MODEL SIRD - COVID-19 w Polsce 2020-2022')
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
fig.autofmt_xdate()
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(date, I_derivative[:len(date)], 'r--', alpha=0.7, linewidth=2, label='Infected Derivative')
ax.plot(date, R_derivative[:len(date)], 'b--', alpha=0.7, linewidth=2, label='Recovered Derivative')
ax.plot(date, D_derivative[:len(date)], 'k--', alpha=0.7, linewidth=2, label='Deceased Derivative')
ax.set_xlabel('Data')
ax.set_ylabel('Tempo zmian')
ax.legend()
ax.set_title('Tempo zmian stanu epidemii COVID-19 w Polsce 2020-2022 MODEL SIRD')
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
fig.autofmt_xdate()

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(date, D[:len(date)], 'k', alpha=0.7, linewidth=2, label='Deceased')
ax.set_xlabel('Data')
ax.set_ylabel('Liczba osób')
ax.legend()
ax.set_title('MODEL SIRD śmiertelność - COVID-19 w Polsce 2020-2022')
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
fig.autofmt_xdate()
plt.tight_layout()
plt.show()