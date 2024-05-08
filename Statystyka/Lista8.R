# Lista 8 Filip Antoniak
# Zadanie 1
# a) ------------------------------------------------------
# 30 (ze 100) studentów  ma iq wyższy niż 115
wariancja = 225
proporcja_sukcesu = 30/100
blad_standardowy_proporcji = sqrt(proporcja_sukcesu*(1-proporcja_sukcesu)/100)
# wyznaczyć przedział ufności dla wszystkich studentów, IQ > 115
# i) Poziom ufności 95% -----------------------------------
przedzial_ufnosci = function(alfa, srednie_iq) {
  wartosc_krytyczna = qnorm(1-alfa/2)
  dolna_granica = proporcja_sukcesu - blad_standardowy_proporcji*wartosc_krytyczna
  print(dolna_granica)
  gorna_granica = proporcja_sukcesu + blad_standardowy_proporcji*wartosc_krytyczna
  print(gorna_granica)
}
przedzial_ufnosci(1-0.95, 109)
# ii) Poziom ufności 99% ----------------------------------
przedzial_ufnosci(1-0.99, 109)

# b) ------------------------------------------------------
#i) w oparciu o wartość krytyczną dla rozkładu normalnego
przedzial_ufnosci_duza_proba = function(alfa, srednia_iq) {
  blad_standardowy = sqrt(wariancja)/sqrt(100)
  wartosc_krytyczna = qnorm(1-alfa/2)
  dolna_granica = srednia_iq - blad_standardowy*wartosc_krytyczna
  print(dolna_granica)
  gorna_granica = srednia_iq + blad_standardowy*wartosc_krytyczna
  print(gorna_granica)
}
przedzial_ufnosci_duza_proba(1-0.95, 109)
#ii)
przedzial_ufnosci_duza_proba(1-0.99, 109)

# c) ------------------------------------------------------
#i) w oparciu o wartość krytyczną dla rozkładu Studenta
przedzial_ufnosci_studenta = function(alfa, srednia_iq) {
  blad_standardowy = sqrt(wariancja)/sqrt(100)
  # qt - wartosc rozkladu studenta
  wartosc_krytyczna = qt(1 - alfa / 2, 100-1)
  dolna_granica = srednia_iq - blad_standardowy*wartosc_krytyczna
  print(dolna_granica)
  gorna_granica = srednia_iq + blad_standardowy*wartosc_krytyczna
  print(gorna_granica)
}
przedzial_ufnosci_studenta(1-0.95, 109)
#ii)
przedzial_ufnosci_studenta(1-0.99, 109)


# Zadanie 2
# a) ------------------------------------------------------
waga<-read.csv2("C:/Users/Filip/Desktop/Studia/Statystyka/waga1.csv")
sredni_wzrost
przedzial_ufnosci_duza_proba(1-0.9, sredni_wzrost)

# b) ------------------------------------------------------
przedzial_ufnosci_studenta(1-0.9, sredni_wzrost)

# c) ------------------------------------------------------
przedzial_ufnosci_bootstrap <- function(dane,alpha = 0.1) {
  n = length(dane)
  N = 1000
  sr = array(0,dim=N)
  for (i in 1:N) {
    # Wybór n obserwacji z zwracaniem
    obserwacje = sample(dane, n, replace = TRUE)
    sr[i] = mean(obserwacje)
  }
  # Sortowanie średnich
  sr = sort(sr)
  
  # Wyrzucamy proporcję 0.5α prób z najmniejszymi średnimi oraz 0.5α prób z największymi średnimi
  wy = N * alpha / 2

  dolna_granica = sr[ceiling(wy) + 1]
  gorna_granica = sr[N - floor(wy)]
  
  # Zwracanie wyników jako lista
  print(dolna_granica)
  print(gorna_granica)
}

przedzial_ufnosci_bootstrap(waga$Wzrost, 1-0.9)


# Zadanie 3
# a) ------------------------------------------------------
studentki = waga[waga$plec==1, "Wzrost"]
srednia_studentek = mean(studentki)
przedzial_ufnosci_duza_proba(1-0.98, srednia_studentek)

# b) ------------------------------------------------------
przedzial_ufnosci_studenta(1-0.98, srednia_studentek)

# c) ------------------------------------------------------
przedzial_ufnosci_bootstrap(studentki, 1-0.98)


# Zadanie 4
# a) ------------------------------------------------------
studenci_168plus = waga[waga$Wzrost > 168, "Wzrost"]
srednia_studentow168 = mean(studenci_168plus)
przedzial_ufnosci_duza_proba(1-0.94, srednia_studentow168)

# b) ------------------------------------------------------
przedzial_ufnosci_bootstrap(studenci_168plus, 1-0.94)


# Zadanie 5
# a) ------------------------------------------------------
studentki_168plus = waga[waga$Wzrost > 168 & waga$plec == 1, "Wzrost"]
srednia_studentek168 = mean(studentki_168plus)

przedzial_ufnosci_duza_proba(1-0.96, srednia_studentek168)
# b) ------------------------------------------------------
przedzial_ufnosci_bootstrap(studentki_168plus, 1-0.96)


