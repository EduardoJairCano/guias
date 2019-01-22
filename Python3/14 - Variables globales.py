# ---------------------------------- 14 - VARIABLES GLOBALES ------------------------------------ #
#   Existen dos tipos de variables: GLOBALES y LOCALES, cada una de ellas cuenta con
#       diferentes propiedades:
#   GLOBALES:
#       - Son declaradas despues de las cabeceras
#       - Solo pueden ser utilizadas como referencia, no es posible modificarlas
#   LOCALES:
#       - Solo se ejecutan en una función
#       - Su valor puede ser modificado


# ---- Variables Globales ----------------------------------------------------------------------- #
#   Declaración de variable global
v_global = "anita lava la tina"


def palindromo(frase):
    #   replace() - Remplaza todos los caracteres en un String por otro
    #       replace("caracter_busqueda", "caracter_remplazo")
    #   Declaración de variable local
    frase = frase.replace(" ", "")
    print("\n Variable local en funcion: {}".format(frase))
    return frase == frase[::-1]


#   No es posible modificar la variable global, sin utilizar una función específica
print("\n Variable global antes: {} ".format(v_global))
resultado = palindromo(v_global)
print("\n Variable global despues: {} ".format(v_global))
print(resultado)


# ---- Modificación Variables Globales ---------------------------------------------------------- #
v_global = "\n\tEsta es una variable global\n"


def variable_global():
    #   Con la palabra reservada global es posible modificar el valor de la misma
    #   Tambien es posible utilizar global para crea una variable global dentro
    #       de una función
    global v_global
    v_global = "\n\tNuevo valor de la variable global\n"


print(" Variable global orginial:\n{}".format(v_global))
variable_global()
print(" Variable global despues de la funcion:\n{}".format(v_global))
