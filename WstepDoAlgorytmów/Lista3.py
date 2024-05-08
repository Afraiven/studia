import random
import matplotlib.pyplot as plt

# Zadanie 1
print("-" * 30)
print("Zadanie 1")
print("-" * 30)

urzad = [["A", 0], ["A", 0],[ "A", 0], ["B", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0], ["E", 0]]
# 0: "A", 1: "B", 2: "C"
typy = {"A": 0, "B": 1, "C": 2, "E": 3}
czasy = [[1,4], [5, 8], [9, 12]]
klienci_typy = [random.randint(0, 2) for _ in range(40)]
klienci = [[x, random.randint(czasy[x][0], czasy[x][1])] for x in klienci_typy]

def pierwszy_indeks(typ, wybrani_klienci):
    if typ == 3:
        return 0
    for i in range(len(wybrani_klienci)):
        if wybrani_klienci[i][0] == typ:
            return i 
        
iterations = 0
podzial = [0, 0, 0, 0]
while True:
    iterations += 1
    if len(klienci) == 0:
        if sum([x[1] for x in urzad]) == 0:
            break

    for okienko in urzad:
        # jesli wolne
        if okienko[1] == 0 and len(klienci) != 0:
            indeks = pierwszy_indeks(typy[okienko[0]], klienci)
            if indeks is not None:
                podzial[typy[okienko[0]]] += 1
                okienko[1] = klienci[indeks][1]
                klienci.remove(klienci[indeks])
        elif okienko[1] > 0:
            okienko[1] -= 1
print(iterations)
print(podzial)

# Optymalizacja pomysły:
# Zamiast brać pierwszego klienta do stanowiska E lepiej byłoby posorotwać
# klintów tak by priorytetowo szli tam ci, których jest najwięcej do danego okienka (ilość x czas)

# Zadanie 2
print("\n","-" * 30)
print("Zadanie 2")
print("-" * 30)

urzad_333 = [["A", 0], ["A", 0],[ "A", 0], ["B", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0]]
urzad_2223 = [["A", 0], ["A", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["E", 0], ["E", 0], ["E", 0]]
urzad_1231 = [["A", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0], ["E", 0]]

klienci_typy_30 = [random.randint(0, 2) for _ in range(30)]
klienci_30 = [[x, random.randint(czasy[x][0], czasy[x][1])] for x in klienci_typy]

def symulacja(wybrany_urzad, klienci_kopia):
    klienci_kopia = klienci_kopia.copy()
    iterations = 0
    while True:
        iterations += 1
        if len(klienci_kopia) == 0:
            if sum([x[1] for x in wybrany_urzad]) == 0:
                break

        for okienko in wybrany_urzad:
            # jesli wolne
            if okienko[1] == 0 and len(klienci_kopia) != 0:
                indeks = pierwszy_indeks(typy[okienko[0]], klienci_kopia)
                if indeks is not None:
                    okienko[1] = klienci_kopia[indeks][1]
                    klienci_kopia.remove(klienci_kopia[indeks])
            elif okienko[1] > 0:
                okienko[1] -= 1
    return iterations


print(f"Czas dla urzedu 333: {symulacja(urzad_333, klienci_30)}")
print(f"Czas dla urzedu 2223: {symulacja(urzad_2223, klienci_30)}")
print(f"Czas dla urzedu 1231: {symulacja(urzad_1231, klienci_30)}")


# Symulacja 100
print("\n","-" * 30)
print("Symulacja 100")
print("-" * 30)

czasy_1 = []
czasy_2 = []
czasy_3 = []
for _ in range(100):
    klienci_typy_30 = [random.randint(0, 2) for _ in range(30)]
    klienci_30 = [[x, random.randint(czasy[x][0], czasy[x][1])] for x in klienci_typy]
    czasy_1.append(symulacja(urzad_333, klienci_30))
    czasy_2.append(symulacja(urzad_2223, klienci_30))
    czasy_3.append(symulacja(urzad_1231, klienci_30))
    
print(f"Średnia dla urzedu (3,3,3) to {sum(czasy_1)/len(czasy_1)}")
print(f"Średnia dla urzedu (2,2,2,3) to {sum(czasy_2)/len(czasy_2)}")
print(f"Średnia dla urzedu (1,2,3,1) to {sum(czasy_3)/len(czasy_3)}")

minimalna = min([min(czasy_1), min(czasy_2), min(czasy_3)])
maksymalna = max([max(czasy_1), max(czasy_2), max(czasy_3)])
hist_bins = [x for x in range(minimalna-1, maksymalna+1)]
plt.figure(figsize=(10, 6)) 
plt.hist(czasy_1, bins=hist_bins, color='blue', alpha=0.5, label='Urząd 1 - (3,3,3)', edgecolor='black')
plt.hist(czasy_2, bins=hist_bins, color='green', alpha=0.5, label='Urząd 2 - (2,2,2,3)', edgecolor='black')
plt.hist(czasy_3, bins=hist_bins, color='red', alpha=0.5, label='Urząd 3 - (1,2,3,1)', edgecolor='black')
plt.xlabel('Czas pracy')
plt.ylabel('Ilość powtórzeń')
plt.title('Histogram zestawienie wydajności urzędów (zestawienie na bazie 100 symulacji 30-stu klientów)')
plt.legend()
plt.show()

