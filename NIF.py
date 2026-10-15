import time
DNI= int(input("Introduzca su DNI para calcular su NIF: "))
restoDNI= DNI % 23
letrasNIF= "TRWAGMYFPDXBNJZSQVHLCKE"
eleccionLetra= letrasNIF[restoDNI]
time.sleep(1)
print("Su NIF es ", str(DNI) + eleccionLetra)
