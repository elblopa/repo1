#Problema 4

pi = 3.1416
r = float(input("Digite el radio en centimetros: "))
h = float(input("Digite el alto en centimetros: "))

area = 2*pi*r*(h+r)
vol = pi*h*r*r

print("Area: ", area)
print("Volumen: ", vol)