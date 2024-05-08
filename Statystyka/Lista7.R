# Lista 7 Filip Antoniak
# Zadanie 1
# a) ------------------------------------------------------
# i) P(X<164)
odchylenie = sqrt(144)
pnorm(164, 170, odchylenie)
# ii) P(X>188) = 1 - P(X<188)
1 - pnorm(188, 170, odchylenie)
# iii) P(158<X<185) = P(X<185) - P(X<158)
pnorm(185, 170, odchylenie) - pnorm(158, 170, odchylenie)

# b) ------------------------------------------------------
qnorm(0.85, 170, odchylenie)

#Zadanie 2
# ---------------------------------------------------------
# i) Z=cos(2πU_1) *√(-2ln⁡(U_2)), gdzie U_1,U_2~U[0,1].
# generowanie 10000 realizacji [0, 1]
n = 10000
U1 = runif(n)
U2 = runif(n)
Z = cos(2*pi*U1)*sqrt(-2*log(U2))
head(Z)

# ii) -----------------------------------------------------
estymator_jadrowy = density(Z)
# standardowy rozkład normalny znormalizowany dla wartsci z zakresu Z
wartosci_X = seq(from=min(Z), to=max(Z), length.out = length(estymator_jadrowy$x))
rozklad_normalny <- dnorm(wartosci_X, mean = 0, sd = 1)

# zestawienie na wykresie
plot(estymator_jadrowy, main="Zestawienie estymatora Z i rozkładu normalnego",
     xlab="Wartości", ylab="Gęstość")
lines(wartosci_X, rozklad_normalny, col='purple', lwd=2)
legend("bottom", legend=c("Estymator jądrowy Z", "Rozkład normalny (0, 1)"),
       col=c("black", "purple"), lwd=2)

# iii) ----------------------------------------------------
Y = 100+15*Z
jadro_Y = density(Y)
wartosci_X = seq(from=min(Y), to=max(Y), length.out = length(jadro_Y$x))
rozklad_normalny <- dnorm(wartosci_X, mean = 100, sd = 15)

# zestawienie na wykresie
plot(jadro_Y, main="Zestawienie estymatora Y i rozkładu normalnego",
     xlab="Wartości", ylab="Gęstość")
lines(wartosci_X, rozklad_normalny, col='red', lwd=2)
legend("bottom", legend=c("Estymator jądrowy Y", "Rozkład normalny (100, sqrt(15))"),
       col=c("black", "red"), lwd=2)


#Zadanie 3
# ---------------------------------------------------------
# i) Wzrost X ma rozkład normalny z średnią 170cm a odchyleniem standardowym 12cm.
wzrost_x = rnorm (2000, 170, 12)
# ii) 
Z = (wzrost_x - 170)/12
jadro_Z = density(Z)

# standardowy rozkład normalny znormalizowany dla wartsci z zakresu Z
wartosci_X <- seq(from=min(Z), to=max(Z), length.out = length(jadro_Z$x))
rozklad_normalny <- dnorm(wartosci_X, mean = 0, sd = 1)

# zestawienie na wykresie
plot(jadro_Z, main="Zestawienie estymatora Z i rozkładu normalnego",
     xlab="Wartości", ylab="Gęstość")
lines(wartosci_X, rozklad_normalny, col='green', lwd=2)
legend("bottom", legend=c("Estymator jądrowy Z", "Rozkład normalny (0, 1)"),
       col=c("black", "green"), lwd=2)

# iii)
# dla n = 500 ---------------------------------------------
wzrost_x = rnorm (500, 170, 12)
Z = (wzrost_x - 170)/12
jadro_Z = density(Z)

# standardowy rozkład normalny znormalizowany dla wartsci z zakresu Z
wartosci_X <- seq(from=min(Z), to=max(Z), length.out = length(jadro_Z$x))
rozklad_normalny <- dnorm(wartosci_X, mean = 0, sd = 1)

# zestawienie na wykresie
plot(jadro_Z, main="Zestawienie estymatora Z i rozkładu normalnego",
     xlab="Wartości", ylab="Gęstość")
lines(wartosci_X, rozklad_normalny, col='green', lwd=2)
legend("bottom", legend=c("Estymator jądrowy Z", "Rozkład normalny (0, 1)"),
       col=c("black", "green"), lwd=2)

# dla n = 100 ---------------------------------------------
wzrost_x = rnorm (100, 170, 12)
Z = (wzrost_x - 170)/12
jadro_Z = density(Z)

# standardowy rozkład normalny znormalizowany dla wartsci z zakresu Z
wartosci_X <- seq(from=min(Z), to=max(Z), length.out = length(jadro_Z$x))
rozklad_normalny <- dnorm(wartosci_X, mean = 0, sd = 1)

# zestawienie na wykresie
plot(jadro_Z, main="Zestawienie estymatora Z i rozkładu normalnego",
     xlab="Wartości", ylab="Gęstość")
lines(wartosci_X, rozklad_normalny, col='green', lwd=2)
legend("bottom", legend=c("Estymator jądrowy Z", "Rozkład normalny (0, 1)"),
       col=c("black", "green"), lwd=2)


#Zadanie 4
# ---------------------------------------------------------
lambda = 1/2
oczekiwana = 1/lambda
odchylenie = oczekiwana
n = 1000
# a) ------------------------------------------------------
# funckja generuje Si, czyli i (ile_x) wartosci x o rozkladzie wykladniczym
badaj_odchylenie = function(ile_x) {
  # 1000 realizacji danych sum
  S = c()
  Z = c()
  for (i in 1:n) {
    # generuj pojedyncza sume
    S[i] = sum(rexp(ile_x, lambda))
    
    # dla każdej (pojedynczej) realizacji, generuje Z z centralnego twierdzenia granicznego
    Z[i] = (S[i] - oczekiwana*ile_x)/(odchylenie * sqrt(ile_x))
  }
  return(Z)
}
Z1 = badaj_odchylenie(1)
Z20 = badaj_odchylenie(20)
Z200 = badaj_odchylenie(200)
abs(mean(head(Z1)))
abs(mean(head(Z20)))
abs(mean(head(Z200)))

# b) ------------------------------------------------------
generuj_zestawienie = function(z, nazwa="") {
  nazwa = paste("Zestawienie estymatora", nazwa, "i rozkładu normalnego")
  plot(density(z), main=nazwa, xlab="Wartości", ylab="Gęstość")
  wartosci_X <- seq(from=min(z), to=max(z), length.out = length(estymator_Z1$x))
  rozklad_normalny <- dnorm(wartosci_X, mean = 0, sd = 1)
  lines(wartosci_X, rozklad_normalny, col='green', lwd=2)
  legend("bottom", legend=c("Estymator jądrowy Z","Rozkład normalny (0, 1)"),
         col=c("black", "green"), lwd=2)
  
}
generuj_zestawienie(Z1, "Z1")
generuj_zestawienie(Z20,"Z20")
generuj_zestawienie(Z200, "Z200")


#Zadanie 5
# odchylenie = sqrt(np*(1-p))
# wartosc oczekiwana = np
histogram_binom = function(n, p) {
  x = 0:n
  ilosc = 10000
  odchylenie = sqrt(n*p*(1-p))
  wartosc_oczekiwana = n*p
  bin_a = rbinom(ilosc, n, p)
  
  #obliczam maksymalna wartosc w gestosci bin_a zeby ustalic wysokosc wykresu (y)
  max_bin_a = max(density(bin_a)$y)
  
  hist(bin_a, freq = FALSE, col = "blue",
       main = paste("Histogram dla rozkładu rbinom n=",n,"p=",p), 
       xlab = "x", ylab = "gęstość prawdopodobieństwa",
       ylim = c(0, max_bin_a*1.15))
  #rozkład normalny
  curve(dnorm(x, mean = wartosc_oczekiwana, sd = odchylenie),
        add = TRUE, lwd = 2, col = "red", from = 0, to = n)
}
# a) ------------------------------------------------------
histogram_binom(30, 0.5)
# b) ------------------------------------------------------
histogram_binom(1000, 0.5)
# c) ------------------------------------------------------
histogram_binom(30, 0.1)
# d) ------------------------------------------------------
histogram_binom(1000, 0.05)

