#Problema 3
from math import pow

x = float(input("X: "))
y = float(input("Y: "))

P = 5*pow(x, 5) + 6*pow(x, 4)*y + 7*pow(x, 3)*pow(y, 2) + 3*pow(x, 2) - 7*x + 6*pow(y, 2)

Q = 4*pow(x, 3) - 8*pow(x, 2) + 12*x - 9

print("P(x, y): ", P)
print("Q(x): ", Q)