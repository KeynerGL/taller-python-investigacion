"""
Lista de compras
Keyner Gallego
"""
totalp = 0

#Cantidad productos

cantidad = int(input("Cuantos productos vas a comprar: " ))

#Pedir nombre y precio
for i in range (cantidad):
    nombreP = input(f"-Nombre del producto {i + 1}-: ")
    precioP = float(input(f"--Precio del Producto {i + 1}--: "))
    totalp = totalp + precioP

#Total a pagar
print(f"Total a pagar: {totalp}")

#Descuento

if totalp > 100:
    descuento = totalp * 0.10
    totalt = totalp - descuento

    print (f"El descuento es {descuento}")
    print (f"Total con descuento: {totalt}")