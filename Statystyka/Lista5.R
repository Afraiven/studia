
#Lista5
#Zadanie 1

#a)
#i)
x <- runif(5000, min = 0, max = 1)
hist(x, main = "Estymator gęstości rozkładu jednostajnego", xlab = "x")

#ii)
x <- density(x)
plot(x, main = "Estymator jądrowy gęstości rozkładu jednostajnego", xlab = "x", ylab = "gęstość")

#b)
#i)
x <- rnorm(3000, mean = 100, sd = 15)
hist(x, main = "Estymator gęstości rozkładu normalnego", xlab = "x")

#ii)
x <- density(x)
plot(x, main = "Estymator jądrowego gęstości rozkładu normalnego", xlab = "x", ylab = "gęstość")

#Zadanie 2
#i)
rzuty <- floor(runif(600, min = 1, max = 7))

srednia <- mean(rzuty)
wariancja <- var(rzuty)

cat("Średnia wynosi:", srednia, "Porównanie z wartością teoretyczną:", 3.5, "\n")
cat("Wariancja wynosi:", wariancja, "Porównanie z wartością teoretyczną:", 35/12, "\n")

czestosci <- table(rzuty)

cat("Rozkład częstości dla wyników:\n")
print(czestosci)

rozklad_jednostajny <- rep(1/6, 6)
cat("Dyskretny rozkład jednostajny:\n")
print(rozklad_jednostajny)

#ii)
freq_table <- table(rzuty)
df_freq <- as.data.frame(freq_table)

#iii)
rzuty <- sample(1:6, 600, replace=TRUE)

srednia <- mean(rzuty)
wariancja <- var(rzuty)
czestosci <- table(rzuty)

#Zadanie 3
#i)
x <- sample(0:3, 1000, replace = TRUE, prob = c(0.3, 0.4, 0.2, 0.1))

mean(x)
var(x) 

#ii)
mean_x <- mean(x) # średnia z próby
sd_x <- sd(x) # odchylenie standardowe z próby

#iii)
freq_table <- table(x)
freq_table

#Zadanie 4
#i)
n <- 10
p <- 0.3
results <- rbinom(100, n, p)

#ii)
p <- 0.4
results <- rgeom(50, p)

#Zadanie 5
#i)
lambda <- 3
n <- 50
results <- numeric(n)
i <- 1

while (i <= n) {
  u <- runif(1)
  x <- 0
  p <- exp(-lambda)
  F <- p
  
  while (u > F) {
    x <- x + 1
    p <- p * lambda / x
    F <- F + p
  }
  
  results[i] <- x
  i <- i + 1
}


#Zadanie 6
#i)
#ii)
n <- 200
F_inv <- function(u) sqrt(4*u) # definicja odwrotności dystrybuanty
U <- runif(n)
X <- F_inv(U) 

#iii)
#iv)
n <- 200 
X <- numeric(n) 
i <- 1 
while(i <= n){
  
  x <- runif(1, min = 0, max = 2)
  y <- runif(1)
  
  if(y <= 0.5*x){
    X[i] <- x 
    i <- i + 1
  }
}
