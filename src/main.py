""" 
Programa: Hola Mundo Interactivo 
Descripción: Programa que saluda al usuario y muestra un menú de opciones 
Autor: Keyner Andrey Gallego Lizarazo
Fecha: 16/mayo/2026
""" 
#Constantes del programa

NOMBRE_PROGRAMA = "Hola Mundo Interactivo"
VERSION = "1.0"
MAX_INTENTOS = 3
ANIO_ACTUAL = 2026

#Parte 1: Saludo Inicial

print("=" * 50)
print(f"    {NOMBRE_PROGRAMA} v{VERSION}")
print("=" * 50)
print()

#solicitar el nombre del usuario

nombre_usuario = input("¿Cual es tu nombre? ")

#Validar el que el nombre no esta vacio

if nombre_usuario == "":
    print("No ingreaste un nombre. Te llamare 'Usuario'")
    nombre_usuario = "Usuario"
else:
    print(f"¡Hola, {nombre_usuario}! Bienvenido/a al programa.")

print()

#Parte 2: Preguntar la Edad

edad_texto = input("¿Cuantos años tienes? ")
edad = int(edad_texto)

if edad < 18:
    print(f"Eres menor de edad, {nombre_usuario}.")
    categoria = "joven"
elif edad >= 18 and edad < 60:
    print(f"Eres adulto, {nombre_usuario}.")
    categoria = "adulto"
else:
    print(f"Esres adulto mayor, {nombre_usuario}.")
    categoria = "adulto mayor"

# Calcular el año de nacimiento aprox
anio_nacimiento = ANIO_ACTUAL - edad
print(f"Naciste aproximadamente en el año {anio_nacimiento}")
print()

#Parte 3: Menu de Opciones

print ("=" * 50)
print(" MENU DE OPCIONES")
print("=" * 50)
print("1. Ver tu informacion")
print("2. Contar del 1 al 10")
print("3. Tabla de multiplicar")
print("4. Salir")
print("=" * 50)

#Variable para controlar el menu

continuar = True
intentos_fallidos = 0

while continuar:
    opcion = input("\nElige una opcion (1-4): ")

    #Opcion 1: mostrar informacion del usuario

    if opcion == "1":
        print("\n--- TU INFIRMACION ---")
        print(f"Nombre: {nombre_usuario}")
        print(f"Edad: {edad} años")
        print(f"Categoria: {categoria}")
        print(f"Año de nacimiento: {anio_nacimiento}")
        intentos_fallidos = 0 #reiniciar contador de intentos fallidos
    
    #opcion 2: Contar del 1 al 10

    elif opcion == "2":
        print("\n--- CONTANDO DEL 1 AL 10 ---")
        
        for numero in range (1,11):
            print(f"numero: {numero}")
        intentos_fallidos = 0
    
    #opcion 3: tabla de multiplicar

    elif opcion == "3":
        numero_tabla = input("\n¿De que numero quieres la tabla? ")
        numero_tabla = int(numero_tabla)

        print(f"\n--- TABLA DEL {numero_tabla} ---")
        for i in range (1,11):
            resultado = numero_tabla * i
            print (f"{numero_tabla} x {i} = {resultado}")
        intentos_fallidos = 0
    
    #opcion 4:Salir del programa

    elif opcion == "4":
        print(f"\n¡Hasta luego, {nombre_usuario}!")
        print("Gracias por usar el programa. ")
        continuar = False 
    
    #opcion invalida

    else:
        intentos_fallidos = intentos_fallidos + 1
        print (f"\nOpcion invalida. intento {intentos_fallidos} de {MAX_INTENTOS}")

        if intentos_fallidos >= MAX_INTENTOS:
            print ("Demaciados intentos fallidos. cerrando program...")
            continuar = False

        #Mensaje final

        print ("\n" + "=" * 50)
        print("PROGRAMA FINALIZADO")
        print("=" * 50)