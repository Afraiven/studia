import sympy as sp

t = sp.symbols('t')
T = sp.Function('T')
T_R = sp.symbols('T_R')
k = sp.symbols('k')

dT = sp.diff(T(t), t, t)
dT