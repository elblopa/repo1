n = int(input("Digite un numero entero: "))

valor = ""
while (n>=1):
    r = n%2
    n = n/2
    print(int(r))
    valor += str(int(r))

valor_final = ""
for c in valor:
    valor_final = c + valor_final
print(valor_final)