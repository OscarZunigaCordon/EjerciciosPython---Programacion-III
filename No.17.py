lista = []
lista2 = []
cantidad = int(input("Dijite cuantos numeros desea ingresar: "))
suma = 0

while (cantidad > 0):
    numero = int(input("Dijite un Numero: "))
    lista.append(numero)
    cantidad = cantidad - 1
    if (numero % 2 == 0):
        lista2.append(numero)

    print(f"Los Numeros pares ingresados son: {lista2}")
    for i in lista2:
        suma = suma + i
    print(f"La suma de los numeros pares son: {suma}")