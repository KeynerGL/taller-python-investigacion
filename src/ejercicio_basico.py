"""
Ejercicio Basico: Calculadora de edad
Practica con variables, input, y operaciones basicas
"""

#CONSTANTES
ANIO_ACTUAL = 2026

#Solicitar datos al usuario

print("=== CALCULADORA DE EDAD ===")
nombre = input("Tu nombre: ")
anio_nacimiento = input("¿En que año naciste? ")

# Convertir texto a numero
anio_nacimiento = int(anio_nacimiento)

#Calcular la edad 
edad = ANIO_ACTUAL - anio_nacimiento

# Mostrar resultado
print(f"\nHola {nombre}, tienes {edad} años")

#Usar condicional
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    anos_faltantes = 18 - edad
    print(f"Te faltan {anos_faltantes} años para ser mayor de edad")