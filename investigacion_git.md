# Investigacion Git Basico 
## 1. ¿Que es el stanging area o indice en Git y para que sirve?
   Solucion: El staging area o índice es un área intermedia de Git donde se preparan los archivos antes de hacer un commit.

-Explica la diferencia entre working directory, staging area y repository
        Working directory: es donde se encuentran los archivos que estamos modificando.
        Staging area: es el lugar donde se guardan temporalmente los cambios que irán al commit.
        Repository: es donde Git almacena el historial de commits del proyecto.

-¿Por qué es útil tener esta área intermedia?
        Esta área es útil porque permite elegir exactamente qué cambios guardar en cada commit.
## 2. ¿Que hace el comando git status y por que es importante usarlo frecuentemente?
    Solucion: El comando git status muestra el estado actual del repositorio y permite ver los cambios realizados en los archivos.
    Es importante usarlo frecuentemente porque ayuda a verificar que archivos fueron modificados, cuales estan listos para un commit y cuales aun no han sido agregados.Tambien ayuda a evitar errores antes de guardar cambios.
-Menciona al menos 3 tipos de informacion que proporciona
    Archivos modificados.
    Archivos sin seguimiento.
    Archivo sin seguimiento.
    La rama actual del repositorio.
## 3. Diferencia entre git fetch y git pull
    Solucion:GIT FETCH descarga los cambios del repositorio remoto pero no los aplica automaticamente en la rama actual.
    GIT PULL descarga los cambios y ademas los fusiona automaticamente con la rama en la que estamos trabajando.
    GIT FETCH se usa cuando queremos revisar los cambios antes de mezclarlos con nuestro trabajo.
    GIT PULL se usa cuando queremos actualizar rapidamente el proyecto local.
    GIT FETCH es mas seguro porque permite revisar los cambios antes de hacer el merge.
-¿Cuando usarias uno o otro?
    Usaria GIT FETCH cuando quiero revisar primero los cambios realizados en el repositorio remoto antes de aplicarlos.
    Usaria GIT PULL cuando quiero actualizar rapidamente mi repositorio local con los cambios mas recientes.
-¿Cual es mas seguro y por que?
    GIT FETCH es mas seguro porque permite revisar los cambios descargados antes de fusionarlos con la rama actual, evitando posibles conflictos o errores automaticos
## 4.¿Que es un "merge conflict" y como se resuelve?
    Solucion: Un merge conflict ocurre cuando Git no puede combinar automaticamente los cambios de dos ramas porque ambas modificaron la misma parte de un archivo.
    Para resolverlo, se deben revisar los archivos en conflicto, elegir que cambios conservar o combinar ambos cambios manualmente y luego guardar el archivo. Despues se hace un commit para finalizzar el merge.
-Da un ejemplo de cuando podria ocurrir
    Un merge conflict podria ocurrir cuando dos personas modifican la misma linea de un archivo y luego intentan fusionar sus ramas en el mismo proyecto.
-Describe los pasos basicos para resolverlo
    1. Identificar los archivos que tienen conflicto
    2. Abrir el archivo y revisar los cambios en conflicto
    3. Elegir que cambios conservar o combinar ambos
    4. Guardar el archivo corregido
    5. Usar git add para marcar el conflicto como resuelto
    6. Hacer un commit para finalizar el merge.