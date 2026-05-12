# Investigacion GitHub y Colaboracion
## 1.¿Que es un pull Request(PR) y cual es su proposito
    Solucion:Un Pull Request (PR) es una solicitud para fusionar cambios de una rama a otra en un repositorio de GitHub.
    Su proposito es permitir que otras personas revisen, comenten y aprueben los cambios antes de agregarlos al proyecto principal.

    -¿En que se diferencia de un merge directo?

    Un merge directo fusiona los cambios inmediatamente entre ramas, mientras que un Pull Request permite revisar y discutir los cambios antes de hacer la fusion.
    
    -¿Cuales son las ventajas de usar PRs en proyectos colaborativos?

    .permite revisar el codigo antes de fusionarlo
    .Facilitan la colaboracion entre desarroladores
    .Ayudan a detectar errores 
    .Mantienen mejor organizado el proyecto
    .Permiten comnetar y sugerir mejoras en el codigo
## 2.¿Que es un fork en GitHub y caundo se usa?
    Un fork es una copia de un repositorio de GitHub creada en otra cuenta.
    Se usa cuando una persona quiere modificar o cintribuir a un proyecto sin afectar el repositorio original.

    -Diferencia entre fork y clone

    Un fork crea una copia de un repositorio en la cuenta de GitHub del usuario.
    Un clone descarga una copia del repositorio desde GitHuba al computador local para poder trabajar en el.

    -¿Cómo contribuirías a un proyecto open source usando fork?

    Primero haria un fork del repositorio en GitHub, luego clonaria el proyecto en mi computador, realizar los cambios necesarios, subiria los cambios a mi fork y finalmente crearia un Pull Request para proponer los modificaciones al proyecto original.

## 3.¿Que es el archivo .gitignore y por que es importante?
    El archivo .gitignore es un archivo que le indica a Git que archivos o carpetas no deben subirse al repositorio.
    Es importante por que evita subir archivos innecesarios, temporales o privados que podrian causar errores o desorden en el proyecto.

    -Menciona al menos 5 tipos de archivos que NO deberían subirse a un repositorio Python.

    .Archivos __pycache__
    .Archivos .pyc
    .Carpetas venv
    .Archivos de configuaracion personal del editor 
    .Contraseñas o archivos con datos privados
    .Archivos temporales del sistema

    -¿Qué problemas podrían ocurrir si no usas .gitignore?

    Si no se usa .gitignore, se pueden subir archivos innecesarios o privados al repositorio, causar desordern, aumentar el tamaño del proyecto y generar conflictos entre diferentes computadores o desarroladores

## 4.¿Que son los ussues en GitHub y para que sirven?
    Los issues en GitHub son herramientas para repotar errores, proponer mejoras o registrar tareas dentro de un proyecto.
    Sirven para organizar el trabajo, hacer seguimiento de problemas y facilitar la colaboracion entre los desarrolladores.

    -¿Qué información debería contener un buen issue?

    Un buen issue debe contener un titulo claro, una descripcion del prblema o tarea, pasos para reproducir el error si existe, informacion relevante dek proyecto y y una posible solucion o resultadio esperado.

    -¿Cómo se pueden relacionar issues con commits?

    Los issues se pueden relacionar con commits mencionando el numero del issue en el mensaje del commit o en un Pull Request para mostrar que cambios solucionan o estan relacionados con ese problema.

## Investiga qué es GitHub Actions
    GitHub Actions es una herramienta de GitHub que permite automatizar tareas dentro de un proyecto.
    Se utiliza para ejecutar procesos automaticamente cuando ocurre una aciion en el repositorio, como subir codigo o crear un Pull Request.

    -¿Para qué se utiliza?

    GitHub Actions se utiliza para automatizar tareas como ejecutar pruebas, revisar codigo, compilar proyectos y desplegar aplicaciones automaticamente.

    -Menciona 2 ejemplos de tareas que podrías automatizar

    .Ejecutar pruebas automaticas del codigo
    .Subir automaticamente una aplicacion a un servidor despues de un commit