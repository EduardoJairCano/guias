# ----------------------------------------- 06 - TUPLAS ----------------------------------------- #
#
#   Conjunto de datos, en los cuales se pueden almacenar todo tipo de datos muy parecidos
#       a las listas, solo que en estas, los elementos no pueden ser modificados, cuentan
#       con indices
#   Se podria contemplar como un conjunto de elementos que se utilizaran a lo largo de un
#       programa, de los cuales su valor no va a cambiar


# ---- Tuplas ----------------------------------------------------------------------------------- #
#   Se declara el nombre para la tupla, y su contenido entre (), cada uno de los elementos
#       separado por ,
tupla = ("a", "b", "c", "d", "e")
print(tupla)
#   Para seleccionar algún elemento de la tupla, se tiene que indicar el índice
print(tupla[3])
#   Seleccionar ciertos elementos de la tupla
print(tupla[1:3])
#   Mostrar ciertos elementos con saltos
print(tupla[0::2])
#   Mostrar los elementos de manera inversa
print(tupla[::-1])
