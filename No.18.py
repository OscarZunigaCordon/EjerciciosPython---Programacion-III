lista = []
lista2 = []
contador=0

while (contador!=30):
    numero = int(input("Dijite un Numero: "))
    lista.append(numero)
    if (numero % 2 == 0):
        lista2.append(numero)
        contador=contador+1
print(f"Los Numeros pares son: {lista2}")


