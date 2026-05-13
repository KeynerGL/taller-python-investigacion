# investigacion avanzada git
## 1. ¿Que es Git Rebase y en que se diferencia Git Merge?
    Git Rebase es un comando que mueve o reaplica commits de una rama sobre otra para mantener un historial mas limpio
    Git Merge combina dos ramas creando un nunuevo commit de fusion, mientras que Git Rebase reorganiza los commits como si hubieran sido creados en la misma linea de trabajo.

    -¿Cuando es apropiado usar rebase?

    Es apropiado usar rebase cuando se quiere mantener un hisorial mas ordenado y lineal antes de fusionar cambios.

    -¿Que significa "reescribir la historia" en Git?

    Significa modificar el historial de commits cambiando su orden, contenido o mensajes.

## 2¿Que hace el comando git stash y cuando lo usarias?
    El comando git stash guarda temporalmente cambios no terminados sin hacer un commit.

    -Porporciona un ejemplo de situacion donde seria util

    Seria util si estoy trabajando en un archivo y necesito cambiar rapidamente de rama sin perder los cambios realizados.

    -¿Como recuperas cambios guardados con stash?

    Los cambios guardados se recuperan usando:
    git stash pop, en el terminal

## 3¿Que es un "commit convencional" (Conventional Commits)?
    Es una forma organizada de escribir mensajes de commit siguiendo una estructura estandar.

    -¿Por que es importante seguir una convencion para los mensajes de commit?

    Porque ayuda a entender mejor los cambios realizados y mantiene el proyecto organizado.

    -Ademas de feat:, fix:, docs:, investiga 3 prefijos mas

    style: cambios de formato
    test: agregar o modificar pruebas
    refactor: mejorar codigo sin cambiar su funcionamiento

## 4.¿Que es Git Flow?
    Git flow es un modelo de trabajo basado en rams para organizar el desarrollo de proyectos.

    -Describe brevemente el modelo de branching de Git Flow

    Divide el trabajo en diferentes ramas para desarrollo, produccion y nuevos funcionalidades.

    -¿Que tipos de ramas se usan en Git Flow?

    .main
    .develop
    .feature
    .release
    .hotfix

## 5.Investiga que es un "HEAD detached" en Git
    Un "HEAD detached" ocurre cuando Git no esta apuntando a una rama sino directamente a un commit.

    -¿Como ocurre esta situacion?

    Ocurre al cambiar a un commit especifico usando comandos como:
    git checkout id_del_commit

    -¿Como sales de un HEAD detached?

    se sale cambiando nuevamente a una rama:
    git checkout main

## 6.¿Que hace el comando git log y que opciones utiles tiene?
    El comando git log muestra el historial de commits del repositorio.

    -Investiga al menos 3 flags utiles
    --oneline muestra commits resumidos
    --graph muestra un grafico de ramas
    --all muestra commits de todas las ramas

    -Proporciona un ejemplo de uso
    
    git log --oneline --graph --all