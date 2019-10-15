texto = (input("Escriba un texto: "))

contador = 0
contador2 = 0
for i in texto:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        contador = contador + 1
    elif i!=("a", "e", "i", "o", "u"):
        contador2 = contador+1
print("Las vocales son: ", contador)
print("Las consonantes son: ", contador2)
    