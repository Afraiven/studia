# ---------------------------------------------------------------------------
# Zadanie 1 

#a)
def odlegloscHamminga(a, b):
    if len(a) != len(b):
        raise ValueError("Ciągi muszą mieć taką samą długość")
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff


#b)

klawiatura_sasiedzi = {
    'q': ['w', 'a'], 'w': ['q', 'e', 'a', 's'], 'e': ['w', 'r', 's', 'd'], 'r': ['e', 't', 'd', 'f'],
    't': ['r', 'y', 'f', 'g'], 'y': ['t', 'u', 'g', 'h'], 'u': ['y', 'i', 'h', 'j'], 'i': ['u', 'o', 'j', 'k'],
    'o': ['i', 'p', 'k', 'l'], 'p': ['o', 'l'],
    'a': ['q', 'w', 's', 'z'], 's': ['w', 'e', 'a', 'd', 'z', 'x'], 'd': ['e', 'r', 's', 'f', 'x', 'c'],
    'f': ['r', 't', 'd', 'g', 'c', 'v'], 'g': ['t', 'y', 'f', 'h', 'v', 'b'], 'h': ['y', 'u', 'g', 'j', 'b', 'n'],
    'j': ['u', 'i', 'h', 'k', 'n', 'm'], 'k': ['i', 'o', 'j', 'l', 'm'], 'l': ['o', 'p', 'k'],
    'z': ['a', 's', 'x'], 'x': ['s', 'd', 'z', 'c'], 'c': ['d', 'f', 'x', 'v'], 'v': ['f', 'g', 'c', 'b'],
    'b': ['g', 'h', 'v', 'n'], 'n': ['h', 'j', 'b', 'm'], 'm': ['j', 'k', 'n']
}
klawiatura_alt = {
    'a': 'ą', 'c': 'ć', 'e': 'ę', 'l': 'ł', 'n': 'ń',
    'o': 'ó', 's': 'ś', 'z': 'ż', 'x': 'ź'
}

def sa_sasiadami(a, b):
    return a in klawiatura_sasiedzi.get(b, [])

def sa_alt(a, b):
    return klawiatura_alt[a] == b

def odlegloscHammingaMod(a, b):
    if len(a) != len(b):
        raise ValueError("Ciągi muszą mieć taką samą długość")
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            if sa_sasiadami(a[i], b[i]):
                diff += 1
            elif sa_alt(a[i], b[i]):
                diff += 0.5
            else:
                diff += 2
    return diff

print(f"'nana', 'nańa' {odlegloscHammingaMod('nana', 'nańa')}")

#c)
# 100 słów
slownik = {
    "kot", "kota", "kotem", "kotu", "koty", "kotów",
    "pies", "psa", "psem", "psu", "psy", "psów",
    "dom", "domu", "domem", "domowi", "domy", "domów",
    "drzewo", "drzewa", "drzewem", "drzewu", "drzew", "drzewami",
    "komputer", "komputera", "komputerem", "komputerowi", "komputery", "komputerów",
    "telefon", "telefonu", "telefonem", "telefonowi", "telefony", "telefonów",
    "okno", "okna", "oknem", "oknu", "okien", "oknami",
    "drzwi", "drzwiach", "drzwiami",
    "samochód", "samochodu", "samochodem", "samochodowi", "samochody", "samochodów",
    "stół", "stołu", "stołem", "stołowi", "stoły", "stołów",
    "stołek", "stołka", "stołkiem", "stołki", "stołków",
    "krzesło", "krzesła", "krzesłem", "krzesłami", "krzesłach",
    "szafa", "szafy", "szafie", "szafę", "szafą", "szafami",
    "szafka", "szafki", "szafce", "szafkę", "szafką", "szafkami",
    "szuflada", "szuflady", "szufladzie", "szufladę", "szufladą", "szufladami",
    "lampka", "lampki", "lampce", "lampkę", "lampką", "lampkami",
    "lampa", "lampy", "lampie", "lampę", "lampą", "lampami",
    "laptop", "laptopa", "laptopem", "laptopowi", "laptopy", "laptopów",
    "monitor", "monitora", "monitorem", "monitorowi", "monitory", "monitorów",
    "klawiatura", "klawiatury", "klawiaturze", "klawiaturę", "klawiaturą", "klawiaturami",
    "mysz", "myszy", "myszy", "myszce", "myszkę", "myszą", "myszkami",
    "drukarka", "drukarki", "drukarkę", "drukarką", "drukarkami", "drukarkach"
}

# Levenshtein
def lev(a, b):
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    elif a[0] == b[0]:
        return lev(a[1:], b[1:])
    else:
        return 1+min(
            lev(a[1:], b),
            lev(a, b[1:]),
            lev(a[1:], b[1:])
                     )

def czy_w_slowniku(slowo):
    if slowo in slownik:
        return "OK"
    else:
        najblizsze = [(float('inf'), ''), (float('inf'), ''), (float('inf'), '')]
        for wyraz in slownik:
            odleglosc = lev(slowo, wyraz)
            if odleglosc < najblizsze[2][0]:
                najblizsze[2] = (odleglosc, wyraz)
                najblizsze.sort()
        return [wyraz for _, wyraz in najblizsze]


print(czy_w_slowniku("system"))

# ---------------------------------------------------------------------------
# Zadanie 2

#a)
english_frequencies = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
    'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.253, 'k': 1.772, 'l': 4.025,
    'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
    's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.250,
    'y': 1.974, 'z': 0.074
}

german_frequencies = {
    'a': 7.094, 'b': 1.886, 'c': 2.732, 'd': 5.076, 'e': 16.396, 'f': 1.656,
    'g': 3.009, 'h': 4.577, 'i': 6.550, 'j': 0.268, 'k': 1.417, 'l': 3.437,
    'm': 2.534, 'n': 9.776, 'o': 3.037, 'p': 0.670, 'q': 0.018, 'r': 7.003,
    's': 7.577, 't': 6.154, 'u': 5.161, 'v': 0.846, 'w': 1.921, 'x': 0.034,
    'y': 0.039, 'z': 1.134
}

polish_frequencies = {
    'a': 9.986, 'b': 1.482, 'c': 4.436, 'd': 3.293, 'e': 9.052, 'f': 0.312,
    'g': 1.377, 'h': 1.072, 'i': 8.286, 'j': 2.343, 'k': 3.411, 'l': 3.882,
    'm': 2.911, 'n': 5.600, 'o': 8.598, 'p': 3.101, 'q': 0.003, 'r': 4.571,
    's': 4.946, 't': 3.966, 'u': 2.347, 'v': 0.034, 'w': 4.549, 'x': 0.019,
    'y': 3.857, 'z': 6.566
}

#b)
import re

def zamien_litery(tekst):
    tekst = tekst.lower()
    specjalne_na_normalne = {v: k for k, v in klawiatura_alt.items()}

    zmieniony_tekst = ''.join(specjalne_na_normalne.get(litera, litera) for litera in tekst)
    
    zmieniony_tekst = re.sub(r'[^a-z]', '', zmieniony_tekst)
    return zmieniony_tekst

def czestotliwosci_liter(tekst):
    tekst = zamien_litery(tekst)
    n = len(tekst)
    litery = set(tekst)
    slownik_czestotliwosci = dict()
    for litera in litery:
        slownik_czestotliwosci[litera] = (tekst.count(litera) / n)*100
    angielski = 0
    niemiecki = 0
    polski = 0
    for key, val in slownik_czestotliwosci.items():
        angielski += abs(val - english_frequencies[key])
        niemiecki += abs(val - german_frequencies[key])
        polski += abs(val - polish_frequencies[key])
    if angielski < niemiecki:
        if angielski < polski:
            print("Tekst po angielsku")
        else:
            print("Tekst po polsku")
    else:
        if niemiecki < polski:
            print("Tekst po niemiecku")
        else:
            print("Tekst po polsku")


czestotliwosci_liter('''Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

Panno święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy''')
czestotliwosci_liter('''Oh, Lithuania, mu country, Thou ar't like good health
I never knew till now how precious, till I lost Thee.
Now I see Thy beauty whole, because I yearn for Thee
Oh Holy Maid, who Czestochowa's shrine does't guard
And in the Pointed Gateway shine, and watches't Nowogrodek's pinnacle
As Thou dids't heal me by a miracle (for when my wheeping Mother sought Thy''')


#c)
def samogloski(frequencies):
    samogloski = 'aeiouy' 
    suma_samoglosek = 0
    suma_spolglosek = 0

    for litera, czestosc in frequencies.items():
        if litera in samogloski:
            suma_samoglosek += czestosc
        else:
            suma_spolglosek += czestosc

    return suma_samoglosek, suma_spolglosek


angielskie_gloski = samogloski(english_frequencies)
niemiecki_gloski = samogloski(german_frequencies)
polskie_gloski = samogloski(polish_frequencies)


def czestotliwosci_liter_gloski(tekst):
    samogloski = 'aeiouy' 
    suma_samoglosek = 0
    tekst = zamien_litery(tekst)
    n = len(tekst)
    litery = set(tekst)
    slownik_czestotliwosci = dict()
    for litera in litery:
        slownik_czestotliwosci[litera] = (tekst.count(litera) / n)*100
    for litera, czestosc in slownik_czestotliwosci.items():
        if litera in samogloski:
            suma_samoglosek += czestosc
    
    angielski = abs(angielskie_gloski[0]-suma_samoglosek)
    niemiecki = abs(niemiecki_gloski[0]-suma_samoglosek)
    polski = abs(polskie_gloski[0]-suma_samoglosek)
    if angielski < niemiecki:
        if angielski < polski:
            print("Tekst po angielsku")
        else:
            print("Tekst po polsku")
    else:
        if niemiecki < polski:
            print("Tekst po niemiecku")
        else:
            print("Tekst po polsku")

czestotliwosci_liter_gloski('''Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

Panno święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy''')
czestotliwosci_liter_gloski('''Oh, Lithuania, mu country, Thou ar't like good health
I never knew till now how precious, till I lost Thee.
Now I see Thy beauty whole, because I yearn for Thee
Oh Holy Maid, who Czestochowa's shrine does't guard
And in the Pointed Gateway shine, and watches't Nowogrodek's pinnacle
As Thou dids't heal me by a miracle (for when my wheeping Mother sought Thy''')


# ---------------------------------------------------------------------------
# Zadanie 3

#a)
def najdluzszy_podciag(a, b):
    podciagi = []
    i = 0
    j = 0
    podciag = []
    while i < len(a):
        if a[i] == b[j]:
            podciag.append(a[i])
            if j < len(b)-1:
                j += 1
            i += 1
        else:
            if len(podciag) > 0:
                i -= len(podciag)
                podciagi.append(podciag)
                podciag = []
            if j < len(b) -1:
                j += 1
            else:
                j = 0
                i += 1
    if podciagi:
        return max(podciagi), len(max(podciagi))
    else:
        podciagi.append(podciag)
        return max(podciagi), len(max(podciagi))
            

print(najdluzszy_podciag("konwalia", "zawalina"))

#b)
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

print(lcs("ApqBCrDsEF", "tABuCvDEwxFyz", len("ApqBCrDsEF"), len("tABuCvDEwxFyz")))