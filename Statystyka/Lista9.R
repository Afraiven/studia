# Lista 9 Filip Antoniak
# Zadanie 1
# ---------------------------------------------------------
srednia = 109
wariancja = 225
odchylenie = sqrt(wariancja)
n = 100
# a) ------------------------------------------------------
h0 = "średnie IQ = 105"
mi = 105
# Test Z
blad_standardowy_sredniej = odchylenie / sqrt(n)
t = (srednia - mi) / blad_standardowy_sredniej
p = 2 *(1-pnorm(abs(t))) 
# weryfikuje miare wiarygodnosci na poziomach istotności 5%, 1% i 0.1%
# p = 0.00766
# na poziomach istotności 5% i 1% p < alfa, więc 
# odrzucamy wtedy hipotezę h0, co oznacza, że średnie IQ =/= 105
# ale na poziomie 0.1% 0.007 > 0.001 wtedy h0 bylo by zgodne

wartosc_krytyczna = function(a) {
  return(qnorm(1 - a/2))
}
wartosc_krytyczna_5 = wartosc_krytyczna(0.05)
wartosc_krytyczna_1 = wartosc_krytyczna(0.01)
wartosc_krytyczna_01 = wartosc_krytyczna(0.001) 

wnioski_blad = function(wartosc_z, h){
  cat("Dla statystyki testowej t:", abs(wartosc_z), "\n")
  if (abs(wartosc_z) > critical_value_z_5) {
    if (abs(wartosc_z) > critical_value_z_1) {
      if (abs(wartosc_z) > critical_value_z_01) {
        cat("Mamy bardzo mocne dowody przeciwko h0")
      } else {
        cat("Mamy mocne dowody przeciwko h0")
      }
    } else {
      cat("Mamy dowody przeciwko h0")
    }
  } else {
    cat("Nie mamy dowodów przeciwko h0")
  }
  cat("\n")
  cat("h0: ", h0)
}

wnioski_blad(z)

# b) ------------------------------------------------------
# test Studenta (ze wzoru)
t = (srednia - mi) / (odchylenie / sqrt(n))
dystrybuanta_t_studenta = n - 1
p = 2 * (1 - pt(abs(t), dystrybuanta_t_studenta))

# z uwagi na to, że próba jest duża to odchylenie populacji i próby jest takie same
wnioski_blad(z, h0)


# Zadanie 2
# ---------------------------------------------------------
waga = read.csv2("C:/Users/Filip/Desktop/Studia/Statystyka/waga1.csv")
h0 = "średni wzrost obu płci = 168"
mi = 168
# a) ------------------------------------------------------
# test Z
srednia_wzrostu = mean(waga$Wzrost)
n = length(waga$Wzrost)
odchylenie = sd(waga$Wzrost)

blad_standardowy_sredniej = odchylenie / sqrt(n)
t = (srednia_wzrostu - mi) / blad_standardowy_sredniej
p = 2 *(1-pnorm(abs(t))) 
wnioski_blad(t, h0)

# b) ------------------------------------------------------
# test Studenta
t = (srednia_wzrostu - mi) / (odchylenie / sqrt(n))
dystrybuanta_t_studenta = n - 1
p = 2 * (1 - pt(abs(t), dystrybuanta_t_studenta))
wnioski_blad(t, h0)

# c) ------------------------------------------------------
# t.test()
t_test <- t.test(waga$Wzrost, mu = mi, alternative = "two.sided")
t = t_test$statistic
wnioski_blad(t, h0)


# Zadanie 3
# ---------------------------------------------------------
h0 = "średni wzrost studentów męskich wynosi 172cm"
mi = 172
# a) ------------------------------------------------------
# test Z
srednia_wzrostu = mean(waga[waga$plec==0, "Wzrost"])
n = length(waga$Wzrost)
odchylenie = sd(waga$Wzrost)

blad_standardowy_sredniej = odchylenie / sqrt(n)
t = (srednia_wzrostu - mi) / blad_standardowy_sredniej
p = 2 *(1-pnorm(abs(t))) 
wnioski_blad(t, h0)

# b) ------------------------------------------------------
# test Studenta
t = (srednia_wzrostu - mi) / (odchylenie / sqrt(n))
dystrybuanta_t_studenta = n - 1
p = 2 * (1 - pt(abs(t), dystrybuanta_t_studenta))
wnioski_blad(t, h0)

# c) ------------------------------------------------------
# t.test()
t_test <- t.test(waga[waga$plec==0, "Wzrost"], mu = mi, alternative = "two.sided")
t = t_test$statistic
wnioski_blad(t, h0)


# Zadanie 4
# ---------------------------------------------------------
h0 = "wszyscy studenci (obu płci) średnio przytyli się o 2kg w ciągu tego roku"
mi = 2
# a) ------------------------------------------------------
# test Z
roznica =  waga$Waga_po - waga$Waga_przed
srednia = mean(roznica)
n = length(roznica)
odchylenie = sd(roznica)

blad_standardowy_sredniej = odchylenie / sqrt(n)
t = (srednia - mi) / blad_standardowy_sredniej
p = 2 *(1-pnorm(abs(t))) 
wnioski_blad(t, h0)

# b) ------------------------------------------------------
# test Studenta
t = (srednia - mi) / (odchylenie / sqrt(n))
dystrybuanta_t_studenta = n - 1
p = 2 * (1 - pt(abs(t), dystrybuanta_t_studenta))
wnioski_blad(t, h0)

# c) ------------------------------------------------------
# t.test()
t_test <- t.test(roznica, mu = mi, alternative = "two.sided")
t = t_test$statistic
wnioski_blad(t, h0)


# Zadanie 5
# ---------------------------------------------------------
h0 = "wszyscy studenci (męskich) średnio przytyli się o 4kg w ciągu tego roku"
mi = 4
# a) ------------------------------------------------------
# test Z
roznica =  waga[waga$plec==0, "Waga_po"] - waga[waga$plec==0, "Waga_przed"]
srednia = mean(roznica)
n = length(roznica)
odchylenie = sd(roznica)

blad_standardowy_sredniej = odchylenie / sqrt(n)
t = (srednia - mi) / blad_standardowy_sredniej
p = 2 *(1-pnorm(abs(t))) 
wnioski_blad(t, h0)

# b) ------------------------------------------------------
# test Studenta
t = (srednia - mi) / (odchylenie / sqrt(n))
dystrybuanta_t_studenta = n - 1
p = 2 * (1 - pt(abs(t), dystrybuanta_t_studenta))
wnioski_blad(t, h0)

# c) ------------------------------------------------------
# t.test()
t_test <- t.test(roznica, mu = mi, alternative = "two.sided")
t = t_test$statistic
wnioski_blad(t, h0)

