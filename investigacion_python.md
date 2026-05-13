# Investigacion python 
## 1.¿Que es una variable en Python?
    Una variable en Python es un espacio donde se almacena informacion o datos que pueden cambiar  durante la ejecucion del programa.

    -¿Qué tipos de datos pueden almacenar? (enteros, strings, flotantes, booleanos)

    Las variables pueden almacenar diferentes tipos de datos como enteros (int), texto(string), numeros decimales(float) y valores booleanos (True o False).

    -Da 3 ejemplos de nombres válidos e inválidos para variables

    Validos:
    .nombre_usuario
    .edad
    .totalCompra
    Invalidos:
    .1numero
    .mi-variable
    .class

## 2.¿Qué diferencia hay entre = y == en Python?
    El signo = se utiliza para asignar un valor a una variable.
    El signo == se utiliza para comparar dos valores y verificar si son iguales

    -Explica con ejemplos

    nombre = "Keyner"
    En este ejemplo = asigna un valor al varible nombre
    if nombre == "Keyner"
        print("Son iguales")
    En este ejemplo == compara la variable 

## 3.¿Qué es la indentación en Python y por qué es importante?
    La indentacion en Python es el espacio que se deja al inicio de una linea de codigo para organizar bloques de instrucciones.
    Es importante porque Python usa la indentacion para identificar que codigo pertence a ciclos, funciones o condicionales.

    -¿Que pasa si no indentas correctamente tu codigo?

    Si no se indenta correctamente el codigo, Python genera errores y el programa no se ejecuta correctamente porque no puede identificar los bloques de instrucciones.

## 4.Diferencia entre ciclo for y ciclo while
    El ciclo for se utiliza cuando se conoce la cantidad de repeticiones que tendra el programa
    El ciclo while se utiliza cuando el ciclo debe repetirse mientras una condicion sea verdadera 

    -¿Cuando usarias cada uno?

    Usaria for cuando necesito repetir una accion una cantidad especifica de veces.
    Usaria while cuando no se exactamente cuantas veces de repetira el ciclo y depende de una condicion.

    -Da un ejemplo de cada uno

    for i in range(5):
        print(i)
    
    contador = 0

    while contador < 5:
        print(contador)
        contador = contador + 1
    
## 5.¿Que hace la funcion range() en Python?
    La funcion range() se utiliza para generar una secuencia de numeros en un ciclo for

    -Explica range(5), range(1, 10) y range(0, 10, 2)

    range(5) genera numero del 0 al  4
    range(1, 10) genera numeros del 1 al 9
    range(0, 10, 2) genera numeros del 0 al 8 de dos en dos