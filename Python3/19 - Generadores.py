# -------------------------------------- 19 - GENERADORES --------------------------------------- #
#
#   Su función es la de crear un objeto sin necesidad de que sean almacendos en la memoria
#       RAM. Su forma de trabajo es por medio de un ciclo For o While


# ---- Generadores ------------------------------------------------------------------------------ #
#   Declaración de un Generador, se utilizara la palabra reservada YIELD para poder iterar
#       con un valor, que en este caso es tipo Int
def generdor(*args):
    for valor in args:
        yield valor * 10


for valor in generdor(1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(valor)
#   Siempre que se utilice un generador, es necesario emplear YIELD para poder iterar con
#       los valores empleados
