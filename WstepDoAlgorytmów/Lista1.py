# Filip Antoniak
# INS - Wstęp do algortymów #L
# Lista 1
import numpy as np
from random import randint

# Zadanie 1 ---------------------------------------------------------
print("Zadanie 1 ---------------------------------------------------------")
# m wierszy, n kolumn
m, n = 10, 5

oceny = [x/2 for x in range(4, 12)]
macierz = np.matrix([[oceny[randint(0, 7)] for x in range(n)] for _ in range(m)])
print("Wylosowana macierz to:")
print(macierz)

def nie_zdali_n_przedmiotow(n, matrix):
    matrix = matrix.copy()
    matrix[matrix < 3.0] = 1
    matrix[matrix >= 3.0] = 0
    return sum([1 for x in matrix.sum(axis=1) if x>= n])

def srednia(matrix):
    max_srednia = matrix.mean(axis=1).argmax() 
    min_srednia = matrix.mean(axis=1).argmin()
    print(f"Najwyższą średnią: {matrix.mean(axis=1).max()} ma student z ocenami: {matrix[max_srednia]}")
    print(f"Najniższą średnią: {matrix.mean(axis=1).min()} ma student z ocenami: {matrix[min_srednia]}")

def najwiecej_max_ocen():
    matrix = macierz.copy()
    max_ocena = macierz.max()
    matrix[matrix != max_ocena] = 0
    matrix[matrix == max_ocena] = 1
    print(f"Najwięcej najwyższych ocen ma student z nr {matrix.sum(axis=1).argmax()} (od 0) jego oceny to {macierz[matrix.sum(axis=1).argmax()]}")

def generuj_histogramy():
    matrix = macierz.copy()
    matrix = matrix.transpose()
    # histogramy z przedmiotów
    # da sie przedstawic je w matplotlibie nie do konca wiem jak interpretowac polecenie
    for przedmiot in matrix:
        print(np.histogram(przedmiot))

def dobre_srednie():
    print("Lista studentów ze średnią nie niższą niż 4.5:")
    result = []
    matrix = macierz.copy()
    zakwalifikowani = matrix.mean(axis=1) >= 4.5
    for i in range(len(zakwalifikowani)):
        if zakwalifikowani[i]:
            print(f"Student(ka) o indeksie {i} z ocenami {matrix[i]}")            
            result.append(matrix[i])
    if len(result) == 0:
        print("NOP skutecznie popsuł średnie, nikt nie ma średniej >= 4.5")

# przykładowa wartość k = 1, bo min. k to 1
k = 1
print()
print(f"Próg n = {k}, takiej ilości przedmiotów (min) nie zdało {nie_zdali_n_przedmiotow(k, macierz)} studentów", )
print()
srednia(macierz)
print()
najwiecej_max_ocen()
print()
generuj_histogramy()
print()
dobre_srednie()
print()

# Zadanie 2 ---------------------------------------------------------
print("Zadanie 2 ---------------------------------------------------------")
# L wierszy, M kolumn

L, M = 2, 2
macierz_1 = np.matrix([[randint(0, 9) for x in range(M)] for _ in range(L)])
macierz_2 = np.matrix([[randint(0, 9) for x in range(M)] for _ in range(L)])

def odleglosc_symetryczna(P, Q):
    odleglosc = 0
    for i in range(L):
        for j in range(M):
            odleglosc += abs(P[i, j] - Q[i, j])
    return odleglosc
print()
print(f"Odległość między macierzami: \n{macierz_1}\n oraz \n{macierz_2}\n wynosi {odleglosc_symetryczna(macierz_1, macierz_2)}")
print()

# Zadanie 3 ---------------------------------------------------------
print("Zadanie 3 ---------------------------------------------------------")
# macierz n x (n+1)
n = 2
macierz = np.array([[randint(-9, 9) for x in range(n+1)] for _ in range(n)], dtype=float)
print(f"Wygenerowana macierz [{n} x { n+1 }]:\n{macierz}")

def schodki(matrix):
    wiersze, kolumny = matrix.shape
    macierz = matrix.copy()
    wiersz = 0
    kolumna = 0
    while kolumna < kolumny:
        while wiersz < wiersze:
            # przekształcam wiersze tak żeby w miejscach gdzie wiersz == kolumna były 1
            if wiersz == kolumna:
                if macierz[wiersz, kolumna] == 0:
                    maksymalna_wartosc_w_kolumnie = abs(macierz.argmax(axis=0)[kolumna])
                    if macierz.max(axis=0)[kolumna] != 0:
                        tymczasowa = macierz[wiersz].copy()
                        macierz[wiersz] = macierz[maksymalna_wartosc_w_kolumnie]
                        macierz[maksymalna_wartosc_w_kolumnie] = tymczasowa
                    
            wiersz += 1
        kolumna += 1
        wiersz = 0
    wiersz = 0
    kolumna = 0
    while kolumna < kolumny:
        while wiersz < wiersze:
            if wiersz == kolumna:
                if macierz[wiersz, kolumna] !=0:
                    macierz[wiersz] /= macierz[wiersz, kolumna]
            elif kolumna < wiersze:
                if macierz[kolumna, kolumna] != 0:
                    # tutaj niweluje do 0 wartosci wierszy pod elementem "wiodącym"
                    wspolczynnik = macierz[wiersz, kolumna] / macierz[kolumna, kolumna]
                    macierz[wiersz] -= macierz[kolumna] * wspolczynnik
            wiersz += 1
        kolumna += 1
        wiersz = 0
    print("Zredukowana postać schodkowa tej macierzy to:")
    print(macierz)

schodki(macierz)
print()
    
# Zadanie 4 ---------------------------------------------------------
print("Zadanie 4 ---------------------------------------------------------")
# PARAGONY: w kolumnach: numer klienta, numer towaru, liczbę sztuk (lub wagę w kilogramach).
# TOWAR: w kolumnach numer towaru, cenę jednostkową, sposob sprzedaży
paragony = np.array([
    [1023, 1, 3],
    [1023, 4, -3],
    [1023, 2, 1.23],
    [1024, 1, 2.5],
    [1026, 99, 10],
    [1025, 3, 3],
    [1025, 2, 10],
    ], dtype=float)
# normalizacja danych: cena za sztuke oznaczona liczbą 1 a na kg liczbą 0
towar = np.array([
    [1, 10, 1],
    [2, 1, 0],
    [3, 3, 1],
    [4, 8, 0],
    [5, 2.50, 1],
    [6, 3, 1],
    ], dtype=float)

# łączna cena jest liczona tylko z paragonów, które są prawidłowe
ceny_paragonu_na_osobe = dict()
for paragon in paragony:
    prawidlowy = 0
    if paragon[0] not in ceny_paragonu_na_osobe:
        ceny_paragonu_na_osobe[paragon[0]] = 0
    x = towar[towar[:, 0] == paragon[1]]
    # sprawdza czy towar w bazie
    if len(x) == 0:
        print("BŁĄD NA PARAGONIE")
        print(f"Produkt o numerze {paragon[1]} nie jest dostępny w bazie.")
    else:
        # sprawda czy sposob sprzedazy sie zgadza
        if int(paragon[2]) != paragon[2] and x[0][2] == 1:
            print("BŁĄD NA PARAGONIE")
            print(f"Produkt o numerze {paragon[1]} wartość sztuk nie jest całkowita.")
        else:
            prawidlowy += 1
           
    if paragon[2] < 0: 
        print("BŁĄD NA PARAGONIE")
        print(f"Produkt o numerze {paragon[1]} wartość sztuk jest ujemna.")
    else:
        prawidlowy += 1
    if prawidlowy == 2:
        ceny_paragonu_na_osobe[paragon[0]] += paragon[2] * x[0][1]
print()
for klient, cena in ceny_paragonu_na_osobe.items():
    print(f"Klient {klient} zapłacił {cena}")
