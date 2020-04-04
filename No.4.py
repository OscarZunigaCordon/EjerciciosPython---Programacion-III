lista=[]
cantidad=3
while(cantidad>0):
        numero=int(input("Dijite un Numero: "))
        lista.append(numero)
        cantidad=cantidad-1

mayor=max(lista)
print(f"El numero mayor es: {mayor}")