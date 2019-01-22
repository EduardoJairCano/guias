# ----------------------------------------- 03 - STRINGS ---------------------------------------- #
#
#   Conjuntos de cadenas que pueden ser almacenadas en una variable
#   Dato primitivo
#   Las variables String no pueden ser modificadas


# ---- String en variable ----------------------------------------------------------------------- #
#   Declaración de variables tipo string, texto entre comillas dobles o simples
string = " Hola Mundo!"
print("\n String: ", string)
#   Para impirmir texto tipo parrafo se emplean tres comillas dobles o simples
parrafo = """
    Este
    es
    un
    parrafo
    con
    saltos
    de linea
    """
print(parrafo)


# ---- Concatenación de Strings ----------------------------------------------------------------- #
#   Solo se pueden hacer dos tipos de operación para las variables tipo String
#       Suma y Multiplicación
a = " Hola "
b = " Mundo "
print(" Suma de variables : ", a+b)
print(" Multplicación de variables : ", a*3, "\n")
#   Existen tres formas de impirmir texto con variables
#   1) Unio de texto y variables, No es del todo Correcto
string_sumatorio = " Sumatorio:\tLa union de '" + a + "' con '" + b + "'"
print(string_sumatorio)
#   2) Utilizando el operador %s para string
string_porcentaje = " Porcentaje:\tLa union de '%s' con '%s'" % (a, b)
print(string_porcentaje)
#   3) Utilizando el metodo format
string_format = " Format:\tLa union de '{}' con '{}'".format(a, b)
print(string_format)


# ---- Strings como Listas ---------------------------------------------------------------------- #
#   Un String puede cumplir la función de una lista o un arreglo, en los cuales se puede
#       posicionar el puntero en una posición específica en un caracter de la cadena de texto
string_lista = "Lista"
# Imprime el caracter en la posicion 0
print(string_lista[0])
# Imprime el caracter en la posicion 1 y 2
print(string_lista[1], string_lista[2])
# Recorridos de x posicion hasta x posicion en un String
print(string_lista[1:4])
# Recorridos de x posicion hasta x posicion en un String, con saltos de caracteres
# [posicion_incial:posicion_final:salto_de_caracteres]
print(string_lista[0:5:2])
# Recorrido inverso del String
print(string_lista[::-1])
