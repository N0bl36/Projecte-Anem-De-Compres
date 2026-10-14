DNI= input("Introduzca su DNI: ")
Preu= float(input("Introduzca el precio: "))
Descompte= float(input("Introduzca el descuento: "))
IVA= float(input("Introduzca el IVA: "))

importDescompte= Preu * Descompte / 100
preuDescompte= Preu - importDescompte

importIVA= preuDescompte * IVA / 100
preuFinal= preuDescompte + importIVA

print("--------------------------------")
print("TIQUET DE COMPRA")
print("--------------------------------")
print("DNI: ", DNI)
print("Precio inicial: ", Preu)
print("Descuento: ", Descompte, "%")
print("Importe del descuento: ", importDescompte)
print("IVA: ", IVA, "%")
print("Importe del IVA: ", importIVA)
print("--------------------------------")
print("Precio final: ", preuFinal)
print("--------------------------------")