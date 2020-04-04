contador=int(0)
dividendo = int(input("Dijite el dividendo: "))
divisor = int(input("Dijite el divisor: "))

dividendo=dividendo-divisor
while(dividendo >= 0):
    contador=contador+1
    dividendo=dividendo-divisor
print(f"El resultado es:  {contador}")