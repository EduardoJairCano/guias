# ----------------------------------------- 16 - LAMBDA  ---------------------------------------- #
#   Son funciones anónimas, es decir, no es necesario crear una función como tal basta con
#       declara por medio de la palabra reservada LAMBDA más los argumentos que necesitará
#       dicho proceso
#   Se pueden contemplar como pequeñas funciones que pueden ser programadas en una sola
#       linea de código


# ---- Lambda ----------------------------------------------------------------------------------- #
#   Se declara el nombre de la función o proceso, y se iguala a la palabra reservada
#       LAMBDA seguido de los argumentos necesarios para la función, despues de dos puntos
#       se escribe la operación que se desea realizar
#   Nombre_Función = LAMBDA argumentos, .. , .. : operación_a_realizar

#   Forma del Tutorial:
#   funcion = lambda argumento_01, argumento_02: argumento_01 + argumento_02
#   Forma con AutoPep8:
def funcion(argumento_01, argumento_02): return argumento_01 + argumento_02


print(funcion(10, 20))


#   Dar formato a un texto con lambda
#   Forma Tutorial:
#   formato = lambda sentencia: "¿{}?".format(sentencia)
#   Forma con AutoPep8:
def formato(sentencia): return "¿{}?".format(sentencia)


print(formato("Como estas"))
