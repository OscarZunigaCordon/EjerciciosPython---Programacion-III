y = input("Ingresar Numero: ")
x = int(y)
fact = 1
z = 1
while z <= x:
    fact = fact * z
    z = z + 1
print(f"El numero factorial es: {fact}")