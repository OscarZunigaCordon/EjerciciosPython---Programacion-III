salir = ""
resultado=1
while (salir != "f"):
    salir = str(input("Dijite Un Numero: "))
    if (salir != "f"):
        print(f"El resultado es:  {salir}")
        resultado=resultado*int(salir)
        print(resultado)
    else:
        print("Usted ha salido del programa")