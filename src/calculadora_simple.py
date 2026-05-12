"""
Ejercicio: Calculadora
De Keyner Gallego
"""
print("\n=== CALCULADORA DE KEYNER GALLEGO ===")

#pedir dos numeros
num_1 = int(input("Dame el primer numero: "))
num_2 = int(input("Dame el segundo numero: "))

#menu de opciones de calculadora

print("=" * 50)
print("MENU DE SIMBOLOS")
print("=" * 50)
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

#Cariable del menu

continuar = True

while continuar:
    opcion = input("\nElige una operacion: (1-5): ")

    #opcion 1: Suma

    if opcion == "1":
        suma = num_1 + num_2
        print(f"\nLa suma de {num_1} y {num_2} es: {suma}")
    #opcion 2: Resta
    elif opcion == "2":
        resta = num_1 - num_2
        print(f"\nLa resta de {num_1} y {num_2} es: {resta}")
    #opcion 3: Multiplicar
    elif opcion == "3":
        multiplicacion = num_1 * num_2
        print(f"\nLa multiplicacion de {num_1} y {num_2} es: {multiplicacion}")
    #opcion 4: Divicion
    elif opcion == "4":
        divicion = num_1 / num_2
        print(f"\nLa divicion de {num_1} y {num_2} es: {divicion}")
    #opcion 5: Salir
    elif opcion == "5":
        print("Hasta Luego, Gracias por Usar La calculadora")
        continuar = False
    #ERROR
    else:
        print("ERROR Vuelve a ejecutar el programa")
        print("PROGRAMA FINALIZADO")
        continuar = False