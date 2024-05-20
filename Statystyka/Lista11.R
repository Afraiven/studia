# Lista 10 Filip Antoniak
# Zadanie 1

frekwencja = c(171, 200, 168, 213, 226, 222)
rzuty = data.frame(Wynik = c(1, 2, 3, 4, 5, 6),
                   Frekwencja = frekwencja)

# h0 = kostka jest symetyczna
# a) --------------------------------------------------------
oczekiwana_frekwencja = sum(frekwencja) / 6
oczekiwane_rzuty = data.frame(Wynik = c(1, 2, 3, 4, 5, 6),
                   Oczekiwana_frekwencja = oczekiwana_frekwencja)

# b) --------------------------------------------------------
# chi-kwadrat
t = sum((frekwencja - oczekiwana_frekwencja)^2 / oczekiwana_frekwencja)

# c) --------------------------------------------------------
(p = 1 - pchisq(t, 6 - 1))

# d) --------------------------------------------------------
# poziom istotności to 0.05
# p = 0.00693
# p < alfa więc h0 odrzucone
# wiec kostka nie jest symetryczna

# e) --------------------------------------------------------
(chisq.test(frekwencja))


# Zadanie 2
# a) --------------------------------------------------------
# h0= cechy są niezależne
n = 2
m = 2
wyksztalcenie = matrix(c(200, 300, 150, 350), nrow = n, byrow = TRUE)
rownames(wyksztalcenie) = c("Kobiety", "Mężczyźni")
colnames(wyksztalcenie) = c("Wykształcenie Wyższe", "Wykształcenie Średnie")

oczekiwane = matrix(0, nrow = n, ncol = m)
for (i in 1:n) {
  for (j in 1:n) {
    oczekiwane[i, j] = (rowSums(wyksztalcenie)[i] * colSums(wyksztalcenie)[j]) /
      sum(wyksztalcenie)
  }
}
# b) --------------------------------------------------------
t = sum((wyksztalcenie - oczekiwane)^2 / oczekiwane)

# c) --------------------------------------------------------
(p = 1 - pchisq(t, (n - 1) * (m - 1)))

# d) --------------------------------------------------------
# poziom istotności to 0.05
# p = 0.0009165
# p < alfa więc h0 odrzucone
# wiec cechy są zależne

# e) --------------------------------------------------------
(chisq.test(wyksztalcenie))

# f) --------------------------------------------------------
(fisher.test(wyksztalcenie))


# Zadanie 3
# a) --------------------------------------------------------
mieszkania = read.csv2("C:/Users/Filip/Desktop/Studia/Statystyka/mieszkania.csv")
head(mieszkania)
(tabela_rozdzielcza = table(mieszkania$Dzielnica, mieszkania$Pokoje))

# b) --------------------------------------------------------
mieszkania$DuzoPokoi = ifelse(mieszkania$Pokoje >= 4, 4, mieszkania$Pokoje)

# c) --------------------------------------------------------
# h0 = ilość pokoi jest niezależna od dzielnicy
(tabela_rozdzielcza = table(mieszkania$Dzielnica, mieszkania$DuzoPokoi))
chisq.test(tabela_rozdzielcza)
# poziom istotności to 0.05
# p = 0.0017
# p < alfa więc h0 odrzucone
# wiec ilośc pokoi zależy od dzielnicy


# Zadanie 4
# a) --------------------------------------------------------
mieszkania$Drogie = ifelse(mieszkania$Cena/mieszkania$Metraz >= 6000, TRUE, FALSE)
head(mieszkania)

# b) --------------------------------------------------------
tabela_rozdzielcza = table(mieszkania$Dzielnica, mieszkania$Drogie)
chisq.test(tabela_rozdzielcza)
# h0 = prawdopodobieństwo tego, że cena za m2 jest większa niż 6000zł zależy od dzielnicy.
# poziom istotności to 0.05
# p = 7.882e-13
# p < alfa więc h0 odrzucone
# wiec prawdopodobieństwo tego, że cena za m2 jest większa niż 6000zł nie zależy od dzielnicy.


# Zadanie 5
# a) --------------------------------------------------------
# h0 = cena za m2 ma rozklad normalny
mieszkania$Cenam2 = mieszkania$Cena / mieszkania$Metraz
head(mieszkania)

shapiro.test(mieszkania$Cenam2)
plot(density(mieszkania$Cenam2), main = "Estymator gęstości [CENA / M2]", xlab = "[CENA / M2]", ylab = "Wartość")
# poziom istotności to 0.05
# p = 2.2e-16
# p < alfa więc h0 odrzucone

# b) --------------------------------------------------------
# h0 = metraż mieszkań na Śródmieściu ma rozkład normalny.
srodmiescie = mieszkania[mieszkania$Dzielnica == "Srodmiescie", ]
shapiro.test(srodmiescie$Metraz)

plot(density(srodmiescie$Metraz), main = "Estymator gęstości [metrażu mieszkań na Śródmieściu]", xlab = "Metraż", ylab = "Wartość")
# poziom istotności to 0.05
# p = 0.0001493
# p < alfa więc h0 odrzucone


# Zadanie 6
# a) --------------------------------------------------------
wykladnicze = rexp(1000, rate = 1)
# i) h0 = z rozkladu normalnego
ks.test(wykladnicze, "pnorm", mean = 1, sd = 1)
# poziom istotności to 0.05
# p = 2.2e-16
# p < alfa więc h0 odrzucone

# ii) h0 = z rozkladu wykladniczego
ks.test(wykladnicze, "pexp", rate = 1)
# poziom istotności to 0.05
# p = 0.06897
# p > alfa więc brak dowodów by odrzucic h0


# b) --------------------------------------------------------
gamma = rgamma(1000, shape = 100, scale = 1)
# i) h0 = z rozkladu normalnego
ks.test(gamma, "pnorm", mean = 100, sd = 10)
# poziom istotności to 0.05
# p = 0.6647
# p > alfa więc brak dowodów by odrzucic h0
plot(density(gamma))

# ii) h0 = z rozkładu Gamma 
ks.test(gamma, "pgamma", shape = 100, scale = 1)
# poziom istotności to 0.05
# p = 0.5619
# p > alfa więc brak dowodów by odrzucic h0



