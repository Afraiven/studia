# Lista 10 Filip Antoniak
# Zadanie 1
# a) --------------------------------------------------------

# przymuje poziom istotności 5%
n = 1000
proporcja_osob = 385/n
# h0 = 40% populacji ma wykształcenie wyższe
h0 = 0.4
SE = sqrt(h0*(1-h0)/n)
t = (proporcja_osob - h0)/SE
p = 2 * (1 - pnorm(abs(t)))
p
# p =  0.33 > 0.05 więc brak dowodów by odrzucić h0

# b) --------------------------------------------------------
kobiety = 520
kobiety_wyzsze = 220
kobiety_proporcja = kobiety_wyzsze / kobiety
mezczyzni = 480
mezczyzni_wyzsze = 165
mezczyzni_proporcja = mezczyzni_wyzsze / mezczyzni
# h0 = prawdopodobieństwo że osoba kończy studia nie zależy od płci
SE = sqrt(kobiety_proporcja * (1 - kobiety_proporcja) / kobiety + mezczyzni_proporcja * (1 - mezczyzni_proporcja) / mezczyzni)
t = (kobiety_proporcja - mezczyzni_proporcja) / SE
p = 2 * (1 - pnorm(abs(t)))
p

# p = 0.0096 < 0.05 więc są dowody by odrzucić h0, więc to czy
# osoba ukończy studia zależy od płci

prop.test(x=c(kobiety_wyzsze, mezczyzni_wyzsze),n=c(kobiety, mezczyzni))

# c) --------------------------------------------------------
sredni_wzrost_kobiet = 166
wariancja_kobiet = 100
sredni_wzrost_mezczyzn = 174
wariancja_mezczyzn = 121
# h0 = średni wzrost nie zależy od płci
SE = sqrt(wariancja_kobiet/kobiety + wariancja_mezczyzn/mezczyzni)
Z = (sredni_wzrost_kobiet - sredni_wzrost_mezczyzn)/SE
Z
p = 2 * (1 - pnorm(abs(Z)))
p
# p ~ 0 więc są dowody by odrzucić h0, więc średni wzrost zależy od płci

# Zadanie 2
# ---------------------------------------------------------
# h0 = proporcje kobiet wsrod studentow = 0.5
h0 = 0.5
waga = read.csv2("C:/Users/Filip/Desktop/Studia/Statystyka/waga1.csv")
kobiety = sum(waga[waga$plec==1, "plec"])
wszyscy = nrow(waga)
proporcja = kobiety / wszyscy
# a) ------------------------------------------------------
SE = sqrt(h0 * (1 - h0)/wszyscy)
t = (proporcja - h0)/SE
p = 2 * (1 - pnorm(abs(t)))
p

# p = 0.61 > 0.05, brak dowodów by odrzucić h0, proporcje są równe 0.5

# b) ------------------------------------------------------

prop.test(kobiety, wszyscy, p = 0.5)
# Zadanie 3
# ---------------------------------------------------------
# h0 = średnia waga po studiach nie zależy od płci

waga_kobiet_po = mean(waga[waga$plec==1, "Waga_po"])
waga_mezczyzn_po = mean(waga[waga$plec==0, "Waga_po"])
wariancja_kobiet = sd(waga[waga$plec==1, "Waga_po"])^2
wariancja_mezczyzn = sd(waga[waga$plec==0, "Waga_po"])^2

kobiety = sum(waga[waga$plec==1, "plec"])
mezczyzni = nrow(waga) - kobiety

# a) ------------------------------------------------------
SE = sqrt(wariancja_kobiet/kobiety + wariancja_mezczyzn / mezczyzni)
Z = (waga_kobiet_po - waga_mezczyzn_po) / SE
p = 2 * (1 - pnorm(abs(Z)))
p
# p = 0.0005 < 0.05 więc są dowody by odrzucic h0, więc waga po studiach zależy od płci

# b) ------------------------------------------------------
t.test(wagi_kobiet_po, wagi_mezczyzn_po, paired=FALSE)

# Zadanie 4
# ---------------------------------------------------------
kobiety70 = nrow(waga[waga$plec == 1 & waga$Waga_po > 70, ])
mezczyzni70 = nrow(waga[waga$plec == 0 & waga$Waga_po > 70, ])
kobiety = sum(waga[waga$plec==1, "plec"])
mezczyzni = nrow(waga) - kobiety
proporcja_kobiety = kobiety70 / (kobiety)
proporcja_mezczyzn = mezczyzni70 / (mezczyzni)
# h0 = proporcja kobiet ważących więcej niż 70kg po studiach nie różni się
# od proporcji mężczyzn ważących więcej niż 70kg po studiach
SE = sqrt(proporcja_kobiety*(1 - proporcja_kobiety)/kobiety + proporcja_mezczyzn*(1 - proporcja_mezczyzn)/mezczyzni)
t = ( proporcja_kobiety - proporcja_mezczyzn ) / SE
p = 2 * (1 - pnorm(abs(t)))
p
# p = 0.013 < 0.05 więc sa dowody by odrzucic h0, więc proporcje są różne

# b) -------------------------------------------------------
prop.test(x=c(kobiety70, mezczyzni70),n=c(kobiety, mezczyzni))

kob70 = waga[waga$plec == 1, ]
mez70 = waga[waga$plec == 0, ]
t.test(kob70 > 70 , mez70 > 70, paired=FALSE)

# c) -------------------------------------------------------
przedzial_ufnosci_bootstrap_proporcji <- function(dane, conf_level = 0.95) {
  n = nrow(dane)          
  N = 10000               
  sr = array(0,dim=N)      
  
  for (i in 1:N) {
    # Wybór n obserwacji z zwracaniem
    obserwacje = sample(1:n, n, replace = TRUE)
    obserwacje = dane[obserwacje, ]
    
    # Obliczanie proporcji dla kobiet i mężczyzn w próbce
    kobiety70 = sum(obserwacje$plec == 1 & obserwacje$Waga_po > 70)
    mezczyzni70 = sum(obserwacje$plec == 0 & obserwacje$Waga_po > 70)
    all_kobiety = sum(obserwacje$plec == 1)
    all_mezczyzni = sum(obserwacje$plec == 0)
    prop_kobiety = kobiety70 / all_kobiety
    prop_mezczyzni = mezczyzni70 / all_mezczyzni
    
    sr[i] = prop_kobiety - prop_mezczyzni
  }
  
  # Sortowanie 
  sr = sort(sr)
  
  
  # Obliczanie granic przedziału ufności
  alpha <- 1 - conf_level
  
  # Wyrzucamy proporcję 0.5α min i max
  wy = N * alpha / 2
  
  dolna_granica = sr[ceiling(wy) + 1]
  gorna_granica = sr[N - floor(wy)]

  print(dolna_granica)
  print(gorna_granica)
}

przedzial_ufnosci_bootstrap_proporcji(waga, conf_level = 0.95)


# Zadanie 5
# ---------------------------------------------------------
# h0 = średnio mężczyźni są o 5cm wyżsi niż kobiety
k = 5
sredni_mezczyzna = mean(waga[waga$plec==0, "Wzrost"])
srednia_kobieta = mean(waga[waga$plec==1, "Wzrost"])
wariancja_mezczyzna = sd(waga[waga$plec==0, "Wzrost"])^2
wariancja_kobieta = sd(waga[waga$plec==1, "Wzrost"])^2
kobiety = sum(waga[waga$plec==1, "plec"])
mezczyzni = nrow(waga) - kobiety

SE = sqrt(wariancja_mezczyzna/mezczyzni + wariancja_kobieta/kobiety)
Z = ((sredni_mezczyzna - srednia_kobieta) - k ) / SE
p = 2 * (1 - pnorm(abs(Z)))
p
# p = 0.002 < 0.05 więc są dowody by odrzucić h0, średni wzrost jest różny niż 5cm

# Zadanie 6
# ---------------------------------------------------------
# h0 = 80% studentów przybiera na wadze w trakcie studiów
h0 = 0.8
wzrost_wagi = waga["Waga_po"] - waga["Waga_przed"]
n = nrow(waga)
przytyl = wzrost_wagi>0
przytyl = sum(przytyl)
prop.test(przytyl, n, p=0.8)
# p = 0.053 więc h0 jest na granicy bycia odrzuconą dla punktu istotnosci 0.05


# Zadanie 7
# a) -------------------------------------------------------
# h0 = proporcja studentek wyższych od 170cm nie różni się 
# od proporcji studentów wyższych od 170cm
studentki170 = nrow(waga[waga$plec == 1 & waga$Wzrost > 170, ])
studenci170 = nrow(waga[waga$plec == 0 & waga$Wzrost > 170, ])
kobiety = sum(waga[waga$plec==1, "plec"])
mezczyzni = nrow(waga) - kobiety
proporcja_studentki = studentki170 / kobiety
proporcja_studenci = studenci170 / mezczyzni

SE = sqrt(proporcja_studentki*(1 - proporcja_studentki)/kobiety + proporcja_studenci*(1 - proporcja_studenci)/mezczyzni)
t = (proporcja_studentki - proporcja_studenci)/SE
p = 2 * (1 - pnorm(abs(t)))
#p < 0.05 więc są dowody by odrzucic h0, wiec proporcje sie różnią


# b) -------------------------------------------------------

przedzial_ufnosci_bootstrap_proporcji <- function(dane, ufnosc = 0.98) {
  n = nrow(dane)          
  N = 10000               
  sr = array(0,dim=N)      
  
  for (i in 1:N) {
    # Wybór n obserwacji z zwracaniem
    obserwacje = sample(1:n, n, replace = TRUE)
    obserwacje = dane[obserwacje, ]
    
    # Obliczanie proporcji dla kobiet i mężczyzn w próbce
    kobiety70 = sum(obserwacje$plec == 1 & obserwacje$Wzrost > 170)
    mezczyzni70 = sum(obserwacje$plec == 0 & obserwacje$Wzrost > 170)
    all_kobiety = sum(obserwacje$plec == 1)
    all_mezczyzni = sum(obserwacje$plec == 0)
  
    prop_kobiety = kobiety70 / all_kobiety
    prop_mezczyzni = mezczyzni70 / all_mezczyzni
    
    sr[i] = prop_kobiety - prop_mezczyzni
  }
  
  # Sortowanie 
  sr = sort(sr)
  
  # Obliczanie granic przedziału ufności
  alpha <- 1 - ufnosc
  # Wyrzucamy proporcję 0.5α min i max
  wy = N * alpha / 2
  
  dolna_granica = sr[ceiling(wy) + 1]
  gorna_granica = sr[N - floor(wy)]
  
  print(dolna_granica)
  print(gorna_granica)
}

przedzial_ufnosci_bootstrap_proporcji(waga, ufnosc = 0.98)
# -0.5516817
# -0.140678
# wartosci przedziałów < 0 więc proporcja mezczyzn wieksza niz kobiet

