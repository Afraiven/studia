# Zadanie 1
#i
wektor <- c(1/8, 1/4, 1/8, 1/6, 1/6, 1/6)
macierz <- matrix(wektor, nrow=2, byrow=TRUE)
x <- rowSums(macierz)
y <- colSums(macierz)
#ii
wartosci_x <- c(0, 1)
wartosci_y <- c(0, 1, 2)
Ex = sum(wartosci_x*x)
Ey = sum(wartosci_y*y) 
Exy <- 0
for (x in wartosci_x) {
  for (y in wartosci_y) {
    Exy <- Exy + x * y * macierz[x+1, y+1]
  }
}
cov_xy <- (Exy - (Ex*Ey))
var_x = sum(x*wartosci_x^2) - Ex^2
var_y = sum(y*wartosci_y^2) - Ey^2
wsp_korelacji <- cov_xy/sqrt(var_x*var_y)
wsp_korelacji
#iii
Px <- rowSums(macierz)
# Y = {0, 1, 2} dla X = 0
P_Y_given_X0 <- macierz[1, ] / Px[1]
# Y = {0, 1, 2} dla X = 1
P_Y_given_X1 <- macierz[2, ] / Px[2]
P_Y_given_X0
P_Y_given_X1


#Zadanie 2
#a)
#i)

prob <- c(1/8, 1/4, 1/8, 1/6, 1/6, 1/6)

p <- matrix(prob, nrow = 2, byrow = TRUE)

px <- rowSums(p)
py <- colSums(p)

pary <- 
  
  n <- 1000

for (i in 1:n) {
  u <- runif(1)
  
  j=1
  while(u>0){
    u = u-px[j]
    j = j+1
    
  }
  x = j-2
  
  u <- runif(1)
  j=0
  while(u>0){
    j = j+1
    u = u-py[j]
    
    
  }
  y = j-1
  
  pary[i]=c(x,y)
}

pary <- matrix(pary, nrow = 2)
pary

#ii)
p <- matrix(prob, nrow = 2, ncol = 6, byrow = TRUE)

X <- c(0, 1)
Y <- c(0, 1, 2)

cov_mat <- cov(X, Y, p)

# współczynnik korelacji Pearsona
cor_pearson <- cor(X, Y, method = "pearson")
cor_pearson

# współczynnik korelacji Spearmana
cor_spearman <- cor(X, Y, method = "spearman")

# współczynnik korelacji Kendalla
cor_kendall <- cor(X, Y, method = "kendall")

#iii)
X <- c(0, 1)
Y <- c(0, 1, 2)
p <- matrix(c(1/8, 1/4, 1/8, 1/6, 1/6, 1/6), nrow = 2, byrow = TRUE, dimnames = list(X, Y))

p


#Zadanie3
#i)

prob <- c(5/100, 3/100, 2/100, 0, 0, 0, 5/100, 7/100, 5/100, 3/100, 0, 0, 3/100, 5/100, 6/100, 4/100, 2/100, 0, 1/100, 4/100, 6/100, 6/100, 2/100, 1/100, 0, 2/100, 5/100, 8/100, 4/100, 1/100, 0, 1/100, 1/100, 2/100, 3/100, 3/100)

mat <- matrix(prob, nrow = 6, byrow = TRUE)
mat

brzeg_X <- rowSums(mat)
brzeg_Y <- colSums(mat)

brzeg_X
brzeg_Y


#ii)
X <- c(2, 3, 3.5, 4, 4.5, 5)
Y <- c(2, 3, 3.5, 4, 4.5, 5)
p <- matrix(c(5/100, 3/100, 2/100, 0, 0, 0, 5/100, 7/100, 5/100, 3/100, 0, 0, 3/100, 5/100, 6/100, 4/100, 2/100, 0, 1/100, 4/100, 6/100, 6/100, 2/100, 1/100, 0, 2/100, 5/100, 8/100, 4/100, 1/100, 0, 1/100, 1/100, 2/100, 3/100, 3/100), nrow = 6, byrow = TRUE, dimnames = list(X, Y))


Ex <- sum(X * rowSums(p))
Ey <- sum(Y * colSums(p))
Exy <- 0
for (x in X) {
  for (y in Y) {
    Exy <- Exy + x * y * p[x+1, y+1]
  }
}

cov_xy <- Exy - Ex * Ey
var_x <- sum(X^2 * rowSums(p)) - Ex^2
var_y <- sum(Y^2 * colSums(p)) - Ey^2
sd_x <- sqrt(var_x)
sd_y <- sqrt(var_y)

rho <- cov_xy / (sd_x * sd_y)
rho # wsp korelacji

#iii)
p <- matrix(prob, nrow = 6, byrow = TRUE)
px <- rowSums(p)
py_x2  <- p[1, ] / px[1]
py_x3  <- p[2, ] / px[2]
py_x35 <- p[3, ] / px[3]
py_x4  <- p[4, ] / px[4]
py_x45 <- p[5, ] / px[5]
py_x5  <- p[6, ] / px[6]

#iv)
X <- c(2, 3, 3.5, 4, 4.5, 5)
Y <- c(2, 3, 3.5, 4, 4.5, 5)
p <- matrix(c(5/100, 3/100, 2/100, 0, 0, 0, 5/100, 7/100, 5/100, 3/100, 0, 0, 3/100, 5/100, 6/100, 4/100, 2/100, 0, 1/100, 4/100, 6/100, 6/100, 2/100, 1/100, 0, 2/100, 5/100, 8/100, 4/100, 1/100, 0, 1/100, 1/100, 2/100, 3/100, 3/100), nrow = 6, byrow = TRUE, dimnames = list(X, Y))

px <- rowSums(p)

p_y_given_x <- sweep(p, 1, px, "/")

pary <- matrix(nrow = 2, ncol = 1000)

set.seed(123) # SEED
for (i in 1:1000) {
  u <- runif(1)
  x_idx <- which.min(cumsum(px) < u)
  x <- X[x_idx]
  
  u <- runif(1)
  y_prob <- p_y_given_x[x_idx, ] 
  y_idx <- which.min(cumsum(y_prob) < u)
  y <- Y[y_idx]
  
  pary[, i] <- c(x, y)
}
# Wizualizacja IV
head(t(pary))

#v)
mat_rea<-cbind(pary)
tab<-table(pary)
(tab_r<-tab/length(pary[1]))

#vi)
data <- t(pary)
colnames(data) <- c("X", "Y")

cor_pearson <- cor(data[, "X"], data[, "Y"], method = "pearson")
cor_spearman <- cor(data[, "X"], data[, "Y"], method = "spearman")
cor_kendall <- cor(data[, "X"], data[, "Y"], method = "kendall")
cor_pearson
cor_spearman
cor_kendall

