# Lista 12 Filip Antoniak
# Zadanie 1

wagi = list(
  Polacy = c(68, 80, 74, 62),
  Brytyjczycy = c(85, 67, 79, 73),
  Chinczycy = c(60, 66, 57)
)

# a) --------------------------------------------------------
# msk
k = 3
mg = 0
srednia = mean(unlist(wagi))
for (j in 1:k) { 
  nj = length(wagi[[j]])
  srednia_j = mean(wagi[[j]])
  mg = mg + nj*(srednia_j - srednia)*(srednia_j - srednia)
}

# wsk
wg = 0
for (j in 1:k) { 
  nj = length(wagi[[j]])
  srednia_j = mean(wagi[[j]])
  for (i in 1:nj) {
    obserwacja = wagi[[j]][i]
    wg = wg + (obserwacja - srednia_j)*(obserwacja - srednia_j)
  }
}
# csk = msk + wsk
(c = mg + wg)

liczba_obserwacji <- sum(sapply(wagi, length))

(swoboda_mg = k - 1)
(swoboda_wg = liczba_obserwacji - k)
(swoboda_c = liczba_obserwacji - 1)

(sredni_kwadrat_mg = mg / swoboda_mg)
(sredni_kwadrat_wg = wg / swoboda_wg)
(sredni_kwadrat_c = c / swoboda_c)

tabela = data.frame(
  SumaKwadratow = c(mg, wg, c),
  StopnieSwobody = c(swoboda_mg, swoboda_wg, swoboda_c),
  SredniaKwadratow = c(sredni_kwadrat_mg, sredni_kwadrat_wg, sredni_kwadrat_c)
)
tabela

# b) --------------------------------------------------------
(f = sredni_kwadrat_mg / sredni_kwadrat_wg)

# c) --------------------------------------------------------
(p<-1-pf(f,k-1,liczba_obserwacji-k))
# Czy można na poziomie istotności 5% twierdzić że waga nie zależy od narodowości?
# p = 0.066 > 0.05 więc brak dowodów by odrzucić

# d) --------------------------------------------------------
wagi_df = stack(wagi)
colnames(wagi_df) = c("Waga", "Kraj")

(aov = aov(Waga ~ Kraj, data = wagi_df))
summary(aov)
# analiza aov potwierdza wcześniej wyciągniete wnioski, p = 0.0661


# Zadanie 2
# a) --------------------------------------------------------
# h0 = metraż nie zależy od dzielnicy 
mieszkania = read.csv2("C:/Users/Filip/Desktop/Studia/Statystyka/mieszkania.csv")
aov = aov(Metraz ~ Dzielnica, data = mieszkania)
summary(aov)
# p = 5.17e-07 *** więc są bardzo mocne dowody by odrzucic hipoteze h0

# b) --------------------------------------------------------
(tukey = TukeyHSD(aov))
# jeśli p spełnia wymaganie co do istotności to można założyc że różnica dla 
# j-tej pary jest równa diff_j


# Zadanie 3
# a) --------------------------------------------------------
mieszkania$DuzoPokoi = ifelse(mieszkania$Pokoje >= 4, 4, mieszkania$Pokoje)
# aby ominąć błąd w TukeyHSD trzeba ustawić duzopokoi jako czynnik
mieszkania$DuzoPokoi <- as.factor(mieszkania$DuzoPokoi)
# b) --------------------------------------------------------
# h0 = cena za m2 nie zależy od liczby pokoi.
mieszkania$CenaZaM2 = mieszkania$Cena / mieszkania$Metraz

aov = aov(CenaZaM2 ~ DuzoPokoi, data = mieszkania)
summary(aov)
# p = <2e-16 *** < 0.05 
# więc są bardzo mocne dowody by odrzucic hipoteze h0

# c) --------------------------------------------------------
(tukey = TukeyHSD(aov))
# jeśli p spełnia wymaganie co do istotności to można założyc że różnica dla 
# j-tej pary jest równa diff_j
# w każdym wypadku p był niższy niż 0.05 więc są silne / bardzo silne dowody by
# wykazać zależność ilości pokoi od ceny za metraż
# np dla 4 pokojowych jest o 1396[zł / m^2] niższa niż dla 1 pokojowych