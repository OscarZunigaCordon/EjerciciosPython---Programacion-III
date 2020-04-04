numero=1
resultado=0
while (numero > 0):
    numero = int(input("Dijite Un Numero: "))
    if (numero > 0):
        print(f"El resultado es:  {numero}")
        resultado=resultado+numero
        print(resultado)
    else:
        print("Usted ha salido del programa")