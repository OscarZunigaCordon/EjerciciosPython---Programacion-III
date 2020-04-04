primerNumero = int(input("Dijite Primer Numero: "))
segudnoNumero = int(input("Dijite Segudno Numero: "))
n = primerNumero + 1
resultado = 0
for i in range(1, n):
    resultado = resultado + segudnoNumero
    print(resultado)

print(f"El resultado es:  {resultado}")