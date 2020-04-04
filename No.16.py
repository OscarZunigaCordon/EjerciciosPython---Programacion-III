lista = []
numero=0
while (numero%2 == 0):
    numero = int(input("Dijite un Numero: "))
    if (numero%2 == 0):
        lista.append(numero)
        menor = min(lista)
        mayor = max(lista)
        print(f"El numero mayor es: {mayor}")
        print(f"El numero menor es: {menor}")
    else:
        print("Usted ha salido del programa")