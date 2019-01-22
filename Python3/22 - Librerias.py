# ------------------------------------ 22 - LIBRERIAS ------------------------------------ #
#
#   Como ya se manejo anteriormente, los módulos son como las librerias, se emplean para
#        facilitar ciertas tareas, existen librerias especiales de Python3
#

# ---- Random ---------------------------------------------------------------------------- #
#   Esta libreria regresa numermos aleatorios, primero se tendria que importar la libreria
#       por medio de import Random
import random
#   Crea un valor aleatorio entre los parámetros que se aisgnen
valor = random.randint(0,10)
print("\n El valor aleatorio es: ", valor)
#   Si se cuenta con una lista predefinida, de la cual se quiere obtener un valor aleatorio,
#       basta con utilizar la función .choice() de la libreria
lista = [23, "perro", True, 12.31, "parangaricutirimicuaro" ]
valor = random.choice(lista)
print("\n El valor aleatorio de la lista es: ", valor)
#   Por medio de la función .shuffle() podemos alterar el orden de una lista
print(lista)
random.shuffle(lista)
print(lista)


# ---- datetime -------------------------------------------------------------------------- #
#   Esta libreria emplea la fecha del sistema para funciones auxiliares
import datetime
#   Para imprimir la fecha actual se utiliza la función .datetime.now()
print(datetime.datetime.now())


# ---- sys ------------------------------------------------------------------------------- #
#   Esta ibreria permite trabajar con ciertas funciones del sistema propio
import sys

#   El comando .stdout.write() y stdout.flush() permiten escribir en consola
for i in range(10):
    sys.stdout.write("hola ")
    sys.stdout.flush()
