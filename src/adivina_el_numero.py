"""
Ejercicio: Adivinar Numero
Keyner Andrey Gallego Lizarazo
"""
numS = 12
intentos = 0
intentosMax = 5
print("\n=== BIENVENIDO A ADIVINA EL NUMERO ===")

#Codigo intentos

while intentos < intentosMax:
    numero = int(input("Adivina el numero que estoy pensando: "))

    if numero == numS:
        print("LO ADIVINASTE")
        intentos = intentos + 5
    elif numero < numS:
        print("EL NUMERO QUE PIENSO ES MAYOR")
    else:
        print("EL NUMERO QUE PIENSO ES MENOR")
    
    intentos = intentos + 1 
if intentos == intentosMax:
    print("SE TE ACABRON LOS INTENTOS")
    print(f"El Numero Secreto Era ===[{numS}]=== ")
    print("Intentalo de Nuevo")