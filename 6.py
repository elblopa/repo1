#Problema 6

pi = 3.1416
r = float(input("Digite el radio menor: "))
R = float(input("Digite el radio mayor: "))

peri = 2*pi*(R+r)
area = pi*(R*R - r*r)

print("Perimetro: ", peri)
print("Area: ", area)