DNI= int(input("Introduzca su DNI para calcular su NIF: "))
restoDNI= DNI % 23
letrasNIF= "TRWAGMYFPDXBNJZSQVHLCKE"
eleccionLetra= letrasNIF[restoDNI]
print("Su NIF es ", DNI, "-", eleccionLetra)