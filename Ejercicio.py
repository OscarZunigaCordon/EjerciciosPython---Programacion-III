def ejercicio1():
    primerNumero = int(input("Dijite Primer Numero: "))
    segudnoNumero = int(input("Dijite Segudno Numero: "))
    n=primerNumero+1
    resultado=0
    for i in range(1, n):
        resultado=resultado+segudnoNumero
        print(resultado)

    print(f"El resultado es:  {resultado}")

#print(ejercicio1())


def ejercicio2():
    resultado = 1
    while True:
        primerNumero = float(input("Dijite Un Numero: "))
        resultado=resultado*primerNumero
        print(f"El resultado es:  {resultado}")



#print(ejercicio2())


def ejercicio3():
    lista=[]
    cantidad=int(input("Dijite cuantos numeros desea ingresar: "))
    mayor=0

    while(cantidad>0):
        numero=int(input("Dijite un Numero: "))
        lista.append(numero)
        cantidad=cantidad-1

    mayor=max(lista)
    print(f"El numero mayor es: {mayor}")

#print(ejercicio3())


def ejercicio4():
    aux, fib, init = 1, 0, 1
    num = int(input("Ingrese un numero para la sucesion de fibonacci: "))
    if num > 0:
        while init <= num:
            print("[{0}]".format(fib), end=" ")
            aux += fib
            fib = aux - fib
            init += 1
        print()
    else:
        print("El numero debe ser mayor a cero!!")


#print(ejercicio4())


def ejercicio5():
    lista = []
    lista2 = []
    cantidad = int(input("Dijite cuantos numeros desea ingresar: "))
    suma = 0

    while (cantidad > 0):
        numero = int(input("Dijite un Numero: "))
        lista.append(numero)
        cantidad = cantidad - 1
        if(numero%2 == 0):
            lista2.append(numero)

    print(f"Los Numeros pares son: {lista2}")
    for i in lista2:
        suma = suma + i
    print(f"La suma de los numeros pares son: {suma}")


print(ejercicio5())