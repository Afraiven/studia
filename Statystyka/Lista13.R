# Lista 13 Filip Antoniak
# Zadanie 1

oceny = data.frame(Student=c(1, 2, 3, 4, 5, 6),
                 Analiza=c(28, 26, 23, 18, 14, 12),
                 Algebra=c(25, 27, 20, 24, 16, 13))
# a) --------------------------------------------------------
# pearson cor = 0.855, p = 0.03
cor.test(oceny$Analiza, oceny$Algebra)
# spearman rho = 0.886 p = 0.034
cor.test(oceny$Analiza, oceny$Algebra, method="spearman")
# kendall tau = 0.734 p = 0.056
cor.test(oceny$Analiza, oceny$Algebra, method="kendall")

# b) --------------------------------------------------------
# h0 = wyniki z tych egzaminów są nieskorelowane
# testy te wykazują korelacje danych 
# przy p < poziom istotnosci 0.05 (oprocz kendall'a, gdzie p jest na pograniczu)
# więc odrzucamy h0 
# więc wyniki są skorelowane


# Zadanie 2
# a) --------------------------------------------------------
X = rnorm(100)
Y = rnorm(100)

# b) --------------------------------------------------------
# "Niech ρ oznacza współczynnik korelacji między X a Y w całej populacji."
# h0 = ρ(X,Y) = 0, (brak korelacji)

# pearson cor = -0.205, p = 0.04
cor.test(X, Y)
# spearman rho = -0.166 p = 0.098
cor.test(X, Y, method="spearman")
# kendall tau = -0.114 p = 0.09
cor.test(X, Y, method="kendall")

# wszystkie testy wykazują małą korelacje, a wartość p dla dwóch testów jest 
# powyżej poziomu istotnośi więc pomimo małej korelacji brak jest dowodów na
# odrzucenie hipotezy h0, poza tym przy każdym wywołaniu wyniki cor i p są 
# różne (bo X i Y są niezależne)

# KOD OD PROFESORA
# c) --------------------------------------------------------
# generuję próby
n<-100
N<-1000
x = X
y = Y
# wyznaczam współczynniki korelacji oraz wartości bezwzględne
kp<-cor(x,y,method="pearson")
ks<-cor(x,y,method="spearman")
kk<-cor(x,y,method="kendall")
kpa<-abs(kp)
ksa<-abs(ks)
kka<-abs(kk)
cor.test(x,y,method="pearson")
cor.test(x,y,method="spearman")
cor.test(x,y,method="kendall")
# liczba symulacji przy której bezwzględna wartość współczynnika korelacji
# przekracza bezwzględną wartość współczynnika dla próby
np<-0
ns<-0
nk<-0
# testy permutacyjne
for (i in 1:N){
  yp<-sample(y,n) # domyślnie replace=FALSE
  kp1<-cor(x,yp,method="pearson")
  ks1<-cor(x,yp,method="spearman")
  kk1<-cor(x,yp,method="kendall")
  if (abs(kp1)>=kpa) {np<-np+1}
  if (abs(ks1)>=ksa) {ns<-ns+1}
  if (abs(kk1)>=kka) {nk<-nk+1}
}
(pp<-np/N)
(ps<-ns/N)
(pk<-nk/N)

# KOD OD PROFESORA
# d) --------------------------------------------------------
# metoda Bootstrap, liczba symulacji, poziom "istotności"
ns<-1000
alpha<-0.05
kpb<-array(0,dim=ns)
ksb<-array(0,dim=ns)
kkb<-array(0,dim=ns)
xp<-array(0,dim=n)
yp<-array(0,dim=n)
for (i in 1:ns){
  # boot lista wybranych par - ze zwracaniem
  boot<-sample(1:n,n,replace=TRUE)
  for (j in 1:n){
    xp[j]<-x[boot[j]]
    yp[j]<-y[boot[j]]
  }
  kpb[i]<-cor(xp,yp,method="pearson")
  ksb[i]<-cor(xp,yp,method="spearman")
  kkb[i]<-cor(xp,yp,method="kendall")
}
kpb<-sort(kpb)
ksb<-sort(ksb)
kkb<-sort(kkb)
# indeksy dla dolnej i górnej granicy
ind_d<-ns*alpha/2+1
ind_g<-ns*(1-alpha/2)
# przedział ufności dla współczynnika Pearsona
(pup_d<-kpb[ind_d])
(pup_g<-kpb[ind_g])
# przedział ufności dla współczynnika Spearmana
(pus_d<-ksb[ind_d])
(pus_g<-ksb[ind_g])
# przedział ufności dla współczynnika Kendalla
(puk_d<-kkb[ind_d])
(puk_g<-kkb[ind_g])
# KONIEC KODU OD PROFESORA

# e) --------------------------------------------------------
plot(X, Y, xlab="X", ylab="Y")
# punkty tworzą chmure co sugeruje, że miara korelacji empirycznej jest blisko zera


# Zadanie 3
# a) --------------------------------------------------------
V = 0.2*X+sqrt(0.96)*Y

# b) --------------------------------------------------------
# pearson cor = 0.456, p = 1.876e-06
cor.test(X, V)
# spearman rho = 0.451 p = 3.165e-06
cor.test(X, V, method="spearman")
# kendall tau = 0.32 p = 2.188e-06
cor.test(X, V, method="kendall")

# h0 = ρ(X,V) = 0, (brak korelacji)
# wszystkie testy wykazują umiarkowaną korelacje, a wartość p są znacznie
# poniżej poziomu istotnośi sa duże dowody by odrzucic h0
# więc jest korelacja, co ma sens bo V nie jest niezależne od X
# chociaż wartości korelacji są przy niektórzych wywołaniach mniejsze
# może to wynikać, z tego, że na wartość V większy wpływ ma Y
# ponieważ 0.2 < sqrt(0.96)

# KOD OD PROFESORA
# c) --------------------------------------------------------
# generuję próby
n<-100
N<-1000
x = X
y = V
# wyznaczam współczynniki korelacji oraz wartości bezwzględne
kp<-cor(x,y,method="pearson")
ks<-cor(x,y,method="spearman")
kk<-cor(x,y,method="kendall")
kpa<-abs(kp)
ksa<-abs(ks)
kka<-abs(kk)
cor.test(x,y,method="pearson")
cor.test(x,y,method="spearman")
cor.test(x,y,method="kendall")
# liczba symulacji przy której bezwzględna wartość współczynnika korelacji
# przekracza bezwzględną wartość współczynnika dla próby
np<-0
ns<-0
nk<-0
# testy permutacyjne
for (i in 1:N){
  yp<-sample(y,n) # domyślnie replace=FALSE
  kp1<-cor(x,yp,method="pearson")
  ks1<-cor(x,yp,method="spearman")
  kk1<-cor(x,yp,method="kendall")
  if (abs(kp1)>=kpa) {np<-np+1}
  if (abs(ks1)>=ksa) {ns<-ns+1}
  if (abs(kk1)>=kka) {nk<-nk+1}
}
(pp<-np/N)
(ps<-ns/N)
(pk<-nk/N)

# KOD OD PROFESORA
# d) --------------------------------------------------------
# metoda Bootstrap, liczba symulacji, poziom "istotności"
ns<-1000
alpha<-0.05
kpb<-array(0,dim=ns)
ksb<-array(0,dim=ns)
kkb<-array(0,dim=ns)
xp<-array(0,dim=n)
yp<-array(0,dim=n)
for (i in 1:ns){
  # boot lista wybranych par - ze zwracaniem
  boot<-sample(1:n,n,replace=TRUE)
  for (j in 1:n){
    xp[j]<-x[boot[j]]
    yp[j]<-y[boot[j]]
  }
  kpb[i]<-cor(xp,yp,method="pearson")
  ksb[i]<-cor(xp,yp,method="spearman")
  kkb[i]<-cor(xp,yp,method="kendall")
}
kpb<-sort(kpb)
ksb<-sort(ksb)
kkb<-sort(kkb)
# indeksy dla dolnej i górnej granicy
ind_d<-ns*alpha/2+1
ind_g<-ns*(1-alpha/2)
# przedział ufności dla współczynnika Pearsona
(pup_d<-kpb[ind_d])
(pup_g<-kpb[ind_g])
# przedział ufności dla współczynnika Spearmana
(pus_d<-ksb[ind_d])
(pus_g<-ksb[ind_g])
# przedział ufności dla współczynnika Kendalla
(puk_d<-kkb[ind_d])
(puk_g<-kkb[ind_g])
# KONIEC KODU OD PROFESORA

# e) --------------------------------------------------------
plot(X, V, xlab="X", ylab="V")
# punkty tworzą chmure podobnie jak przy X, Y ale tym razem jest ona bardziej zbita
# co sugeruje małą korelacje



# Zadanie 4
# a) --------------------------------------------------------
X = rnorm(100)
Y = rnorm(100)
rho = 0.7
V = rho * X + Y*sqrt(1 - rho*rho)

# b) --------------------------------------------------------
H = 170 + 12*X
W = 65 + 10*V
(srednia_H = mean(H))
(sd_H = sd(H))
(srednia_W = mean(W))
(sd_W = sd(W))

# pearson cor = 0.778, p < 2.2e-16
cor.test(H, W)
# spearman rho = 0.72 p < 2.2e-16
cor.test(H, W, method="spearman")
# kendall tau = 0.528 p = 6.354e-15
cor.test(H, W, method="kendall")
# wyniki te wskazują, że jest korelacja i są na to silne dowody

# c) --------------------------------------------------------
plot(density(H), main = "Estymator gęstości H", xlab = "Wzrost", ylab = "Gęstość", col = "green")
plot(density(W), main = "Estymator gęstości W", xlab = "Waga", ylab = "Gęstość", col = "orange")

# d) --------------------------------------------------------
# h0, H i W pochodzą z rozkladu normalnego
# dla H p = 0.04593 < 0.05
shapiro.test(H)
# dla W p = 0.04326 < 0.05
shapiro.test(W)
# co sugeruje że te wartości nie pochodzą z rozkładu normalnego
# odrzucamy hipotezę

# e) --------------------------------------------------------
plot(H, W, main = "Rozrzut zmiennych H i W",
     xlab = "Wzrost", ylab = "Waga", col = "black")
# na wykresie widać, że jest pewna korelacja, co potwierdza testy


# Zadanie 5
# a) --------------------------------------------------------
# a) ------------------PEARSON-------------------------------
# a) --------------------------------------------------------
mieszkania = read.csv2("C:/Users/Filip/Desktop/Studia/Statystyka/mieszkania.csv")
mieszkania$CenaZaM2 = mieszkania$Cena / mieszkania$Metraz

macierz = macierz = matrix(0, nrow = 4, ncol = 4,
                           dimnames = list(c("Metraż", "Liczba pokoi", "Cena", "Cena za m2"),
                                           c("Metraż", "Liczba pokoi", "Cena", "Cena za m2")))
# METRAZ - METRAZ
# cor = 1 p < 2.2e-16 Bardzo silne dowody na pełną korelacje
(corm1 = cor.test(mieszkania$Metraz, mieszkania$Metraz)$estimate)

# METRAZ - POKOJE
# cor = 0.8 p < 2.2e-16 Bardzo silne dowody na mocną korelacje
(corm2 = cor.test(mieszkania$Metraz, mieszkania$Pokoje)$estimate)

# METRAZ - CENA
# cor = 0.78 p < 2.2e-16 Bardzo silne dowody na mocną korelacje
(corm3 = cor.test(mieszkania$Metraz, mieszkania$Cena)$estimate)

# METRAZ - CENA_ZA_M2
# cor = -0.33 p < 2.2e-16 Bardzo silne dowody na ujemną korelacje (niską)
(corm4 = cor.test(mieszkania$Metraz, mieszkania$CenaZaM2)$estimate)

macierz["Metraż", ] = c(corm1, corm2, corm3, corm4)

# LICZBA POKOI) --------------------------------------------------------
# POKOJE - METRAZ
# cor = 0.804 p < 2.2e-16 Bardzo silne dowody na mocną korelacje
corm1 = cor.test(mieszkania$Pokoje, mieszkania$Metraz)$estimate

# POKOJE - POKOJE
# cor = 1 p < 2.2e-16 Bardzo silne dowody na pełną korelacje
corm2 = cor.test(mieszkania$Pokoje, mieszkania$Pokoje)$estimate

# POKOJE - CENA
# cor = 0.6364 p < 2.2e-16 Bardzo silne dowody na średnio mocną korelacje
corm3 = cor.test(mieszkania$Pokoje, mieszkania$Cena)$estimate

# POKOJE - CENA_ZA_M2
# cor = -0.28 p < 2.2e-16 Bardzo silne dowody na ujemną korelacje (niską)
corm4 = cor.test(mieszkania$Pokoje, mieszkania$CenaZaM2)$estimate

macierz["Liczba pokoi", ] = c(corm1, corm2, corm3, corm4)

# CENA) --------------------------------------------------------
# CENA - METRAZ
# cor = 0.788 p < 2.2e-16 Bardzo silne dowody na mocną korelacje
corm1 = cor.test(mieszkania$Cena, mieszkania$Metraz)$estimate

# CENA - POKOJE
# cor = 0.6364 p < 2.2e-16 Bardzo silne dowody na średnio mocną korelacje
corm2 = cor.test(mieszkania$Cena, mieszkania$Pokoje)$estimate

# CENA - CENA
# cor = 1 p < 2.2e-16 Bardzo silne dowody na pełną korelacje
corm3 = cor.test(mieszkania$Cena, mieszkania$Cena)$estimate

# CENA - CENA_ZA_M2
# cor = 0.28 p < 2.2e-16 Bardzo silne dowody na niską korelacje
corm4 = cor.test(mieszkania$Cena, mieszkania$CenaZaM2)$estimate

macierz["Cena", ] = c(corm1, corm2, corm3, corm4)

# CENA_ZA_M2) --------------------------------------------------------
# CENA_ZA_M2 - METRAZ
# cor = -0.33 p < 2.2e-16 Bardzo silne dowody na ujemną korelacje (niską)
corm1 = cor.test(mieszkania$CenaZaM2, mieszkania$Metraz)$estimate

# CENA_ZA_M2 - POKOJE
# cor = -0.283 p < 2.2e-16 Bardzo silne dowody na ujemną korelacje (niską)
corm2 = cor.test(mieszkania$CenaZaM2, mieszkania$Pokoje)$estimate

# CENA_ZA_M2 - CENA
# cor = 0.285 p < 2.2e-16 Bardzo silne dowody na niską korelacje
corm3 = cor.test(mieszkania$CenaZaM2, mieszkania$Cena)$estimate

# CENA - CENA_ZA_M2
# cor = 1 p < 2.2e-16 Bardzo silne dowody na niską korelacje
corm4 = cor.test(mieszkania$CenaZaM2, mieszkania$CenaZaM2)$estimate

macierz["Cena za m2", ] = c(corm1, corm2, corm3, corm4)
macierz
# macierz korelacji Pearsona
#                 Metraż Liczba pokoi      Cena Cena za m2
#Metraż        1.0000000    0.8043183 0.7880057 -0.3319627
#Liczba pokoi  0.8043183    1.0000000 0.6364276 -0.2837147
#Cena          0.7880057    0.6364276 1.0000000  0.2857058
#Cena za m2   -0.3319627   -0.2837147 0.2857058  1.0000000

# b) --------------------------------------------------------
# b) ------------------SPEARMAN------------------------------
# b) --------------------------------------------------------
macierz = macierz = matrix(0, nrow = 4, ncol = 4,
                           dimnames = list(c("Metraż", "Liczba pokoi", "Cena", "Cena za m2"),
                                           c("Metraż", "Liczba pokoi", "Cena", "Cena za m2")))
# METRAZ - METRAZ
(corm1 = cor.test(mieszkania$Metraz, mieszkania$Metraz, method="spearman")$estimate)

# METRAZ - POKOJE
(corm2 = cor.test(mieszkania$Metraz, mieszkania$Pokoje, method="spearman")$estimate)

# METRAZ - CENA
(corm3 = cor.test(mieszkania$Metraz, mieszkania$Cena, method="spearman")$estimate)

# METRAZ - CENA_ZA_M2
(corm4 = cor.test(mieszkania$Metraz, mieszkania$CenaZaM2, method="spearman")$estimate)

macierz["Metraż", ] = c(corm1, corm2, corm3, corm4)

# LICZBA POKOI) --------------------------------------------------------
# POKOJE - METRAZ
corm1 = cor.test(mieszkania$Pokoje, mieszkania$Metraz, method="spearman")$estimate

# POKOJE - POKOJE
corm2 = cor.test(mieszkania$Pokoje, mieszkania$Pokoje, method="spearman")$estimate

# POKOJE - CENA
corm3 = cor.test(mieszkania$Pokoje, mieszkania$Cena, method="spearman")$estimate

# POKOJE - CENA_ZA_M2
corm4 = cor.test(mieszkania$Pokoje, mieszkania$CenaZaM2, method="spearman")$estimate

macierz["Liczba pokoi", ] = c(corm1, corm2, corm3, corm4)

# CENA) --------------------------------------------------------
# CENA - METRAZ
corm1 = cor.test(mieszkania$Cena, mieszkania$Metraz, method="spearman")$estimate

# CENA - POKOJE
corm2 = cor.test(mieszkania$Cena, mieszkania$Pokoje, method="spearman")$estimate

# CENA - CENA
corm3 = cor.test(mieszkania$Cena, mieszkania$Cena, method="spearman")$estimate

# CENA - CENA_ZA_M2
corm4 = cor.test(mieszkania$Cena, mieszkania$CenaZaM2, method="spearman")$estimate

macierz["Cena", ] = c(corm1, corm2, corm3, corm4)

# CENA_ZA_M2) --------------------------------------------------------
# CENA_ZA_M2 - METRAZ
corm1 = cor.test(mieszkania$CenaZaM2, mieszkania$Metraz, method="spearman")$estimate

# CENA_ZA_M2 - POKOJE
corm2 = cor.test(mieszkania$CenaZaM2, mieszkania$Pokoje, method="spearman")$estimate

# CENA_ZA_M2 - CENA
corm3 = cor.test(mieszkania$CenaZaM2, mieszkania$Cena, method="spearman")$estimate

# CENA - CENA_ZA_M2
corm4 = cor.test(mieszkania$CenaZaM2, mieszkania$CenaZaM2, method="spearman")$estimate

macierz["Cena za m2", ] = c(corm1, corm2, corm3, corm4)
macierz
# macierz korelacji Spearmana
#                 Metraż Liczba pokoi      Cena Cena za m2
#Metraż        1.0000000    0.8234866 0.8172369 -0.3981527
#Liczba pokoi  0.8234866    1.0000000 0.6872757 -0.3277168
#Cena          0.8172369    0.6872757 1.0000000  0.1398797
#Cena za m2   -0.3981527   -0.3277168 0.1398797  1.0000000

# c) --------------------------------------------------------
# c) ------------------KENDALL-------------------------------
# c) --------------------------------------------------------
macierz = macierz = matrix(0, nrow = 4, ncol = 4,
                           dimnames = list(c("Metraż", "Liczba pokoi", "Cena", "Cena za m2"),
                                           c("Metraż", "Liczba pokoi", "Cena", "Cena za m2")))
# METRAZ - METRAZ
(corm1 = cor.test(mieszkania$Metraz, mieszkania$Metraz, method="kendall")$estimate)

# METRAZ - POKOJE
(corm2 = cor.test(mieszkania$Metraz, mieszkania$Pokoje, method="kendall")$estimate)

# METRAZ - CENA
(corm3 = cor.test(mieszkania$Metraz, mieszkania$Cena, method="kendall")$estimate)

# METRAZ - CENA_ZA_M2
(corm4 = cor.test(mieszkania$Metraz, mieszkania$CenaZaM2, method="kendall")$estimate)

macierz["Metraż", ] = c(corm1, corm2, corm3, corm4)

# LICZBA POKOI) --------------------------------------------------------
# POKOJE - METRAZ
corm1 = cor.test(mieszkania$Pokoje, mieszkania$Metraz, method="kendall")$estimate

# POKOJE - POKOJE
corm2 = cor.test(mieszkania$Pokoje, mieszkania$Pokoje, method="kendall")$estimate

# POKOJE - CENA
corm3 = cor.test(mieszkania$Pokoje, mieszkania$Cena, method="kendall")$estimate

# POKOJE - CENA_ZA_M2
corm4 = cor.test(mieszkania$Pokoje, mieszkania$CenaZaM2, method="kendall")$estimate

macierz["Liczba pokoi", ] = c(corm1, corm2, corm3, corm4)

# CENA) --------------------------------------------------------
# CENA - METRAZ
corm1 = cor.test(mieszkania$Cena, mieszkania$Metraz, method="kendall")$estimate

# CENA - POKOJE
corm2 = cor.test(mieszkania$Cena, mieszkania$Pokoje, method="kendall")$estimate

# CENA - CENA
corm3 = cor.test(mieszkania$Cena, mieszkania$Cena, method="kendall")$estimate

# CENA - CENA_ZA_M2
corm4 = cor.test(mieszkania$Cena, mieszkania$CenaZaM2, method="kendall")$estimate

macierz["Cena", ] = c(corm1, corm2, corm3, corm4)

# CENA_ZA_M2) --------------------------------------------------------
# CENA_ZA_M2 - METRAZ
corm1 = cor.test(mieszkania$CenaZaM2, mieszkania$Metraz, method="kendall")$estimate

# CENA_ZA_M2 - POKOJE
corm2 = cor.test(mieszkania$CenaZaM2, mieszkania$Pokoje, method="kendall")$estimate

# CENA_ZA_M2 - CENA
corm3 = cor.test(mieszkania$CenaZaM2, mieszkania$Cena, method="kendall")$estimate

# CENA - CENA_ZA_M2
corm4 = cor.test(mieszkania$CenaZaM2, mieszkania$CenaZaM2, method="kendall")$estimate

macierz["Cena za m2", ] = c(corm1, corm2, corm3, corm4)
macierz
# macierz korelacji Kendalla
#                 Metraż Liczba pokoi       Cena  Cena za m2
#Metraż        1.0000000    0.6999691 0.64005614 -0.27608215
#Liczba pokoi  0.6999691    1.0000000 0.56085338 -0.25453267
#Cena          0.6400561    0.5608534 1.00000000  0.09609908
#Cena za m2   -0.2760822   -0.2545327 0.09609908  1.00000000


# d) --------------------------------------------------------

# macierz korelacji Pearsona
#                 Metraż Liczba pokoi      Cena Cena za m2
#Metraż        1.0000000    0.8043183 0.7880057 -0.3319627
#Liczba pokoi  0.8043183    1.0000000 0.6364276 -0.2837147
#Cena          0.7880057    0.6364276 1.0000000  0.2857058
#Cena za m2   -0.3319627   -0.2837147 0.2857058  1.0000000

# macierz korelacji Spearmana
#                 Metraż Liczba pokoi      Cena Cena za m2
#Metraż        1.0000000    0.8234866 0.8172369 -0.3981527
#Liczba pokoi  0.8234866    1.0000000 0.6872757 -0.3277168
#Cena          0.8172369    0.6872757 1.0000000  0.1398797
#Cena za m2   -0.3981527   -0.3277168 0.1398797  1.0000000


# macierz korelacji Kendalla
#                 Metraż Liczba pokoi       Cena  Cena za m2
#Metraż        1.0000000    0.6999691 0.64005614 -0.27608215
#Liczba pokoi  0.6999691    1.0000000 0.56085338 -0.25453267
#Cena          0.6400561    0.5608534 1.00000000  0.09609908
#Cena za m2   -0.2760822   -0.2545327 0.09609908  1.00000000

# duze zwiazki miedzy metrażem a liczbą pokoi, miedzy metrażem a ceną oraz
# ceną i liczbą pokoi

# e) --------------------------------------------------------
# h0 = współczynnik korelacji między ceną za m2 a metrażem wynosi zero 
plot(mieszkania$Metraz, mieszkania$CenaZaM2, main = "Rozrzut zmiennych cenazam2 i metraz",
     xlab = "Metraz", ylab = "Cena za m2", col = "black")

#p < 2.2e-16 dla każdej metody
# co pokazuje, że sa bardzo silne doowdy żeby odrzucic h0
# w rzeczywistosci testy pokazują że wspołcznyyk korelacji wynosi około -0.3 dla każdej metody

