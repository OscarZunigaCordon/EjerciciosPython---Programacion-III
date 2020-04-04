lista = []
cantidad = 30
suma=0
prod=1

while (cantidad > 0):
    numero = int(input("Dijite el numero: "))
    lista.append(numero)
    cantidad = cantidad - 1

for i in lista:
        suma=suma+i

for i in lista:
        prod=prod*i

print(f"La suma de los numeros es: {suma}")
print(f"El producto de los numeros es: {prod}")