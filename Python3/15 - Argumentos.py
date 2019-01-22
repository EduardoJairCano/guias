# --------------------------------- 15 - ARGUMENTOS  ---------------------------------- #
#   Se conoce como ARGUMENTOS a los datos que pueda recibir una función, los cuales
#       pueden ser de cualquier tipo, y en diferente cantidad


# ---- Cantidad de Argumentos -----------------------------------------------------------
#   Como se visualizo anteriormente, la cantidad de argumentos en una función
#       pueden ser declarados por el programador, pero en caso de que el número
#       de ellos sea variable, es posible declaralo con un *
def funcion(*argumentos):
    print(argumentos)
    #   El resultado de la función lo regresara en forma de tupla, para conocer
    #      el tipo de dato de alguna variable se puede utilizar la funcion type()
    print(type(argumentos))


resultado = funcion("Hola ", 20, " Mundo ", True)


# ---- Argumentos con campo específico --------------------------------------------------
#   Es posible asignar argumentos específicos a campos específicos,como resultado
#       la función trabajaria con un Diccionario en vez de una Tupla
def funcion(**kwargs):
    print(kwargs)


#   Al llamar la fucnión, los parametros se tendrian que declarar como Diccionario
resultado = funcion(nombre="Jair", edad=25, estudiante=True)
