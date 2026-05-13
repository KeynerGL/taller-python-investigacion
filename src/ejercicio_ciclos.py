""""
Ejercicio: Practicando Ciclos
Diferentes ejemplos de for y while
"""
print("=== EJERCICO 1: CONTAR NUMEROS ===")
#Ciclo for simple
for i in range(1, 6):
    print(f"contando: {i}")

print("\n=== EJERCICIO 2: SUMA ACUMULATIVA ===")
#usar una variable acumuladora
suma = 0
for numero in range(1, 11):
    suma = suma + numero
    print(f"Suma hasta {numero}: {suma}")

print(f"\nTotal final: {suma}")

print("\n== EJERCICIO 3: PEDIR NUMEROS ===")
#Ciclo while con condicion
contador = 0
while contador < 5:
    numero = input(f"Dame el numero {contador + 1}: ")
    print(f"Guardaste: {numero}")
    contador = contador + 1

print("\n=== EJERCICION 4: NUMEROS PARES ===")
#mostrar solo numeros pares
#ejercio
print("Numeros pares del 1 al 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=" ")
print()