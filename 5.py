#Problema 5

p = float(input("Digite la presión: "))
v = float(input("Digite el volumen: "))
t = float(input("Digite la temperatura: "))

masa = (p*v)/(0.37*(t+460))

print(masa,"gramos")