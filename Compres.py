DNI= input("Introduzca su DNI: ")
Preu= float(input("Introduzca el precio: "))
Descompte= float(input("Introduzca el descuento: "))
IVA= float(input("Introduzca el IVA: "))

print("Su DNI es: ", DNI)
preuDescompre= Preu - (Preu * Descompte / 100)
preuFinal= preuDescompre + (preuDescompre * IVA / 100)
print("El precio final es: ", preuFinal)