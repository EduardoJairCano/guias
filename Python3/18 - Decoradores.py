# -------------------------------------- 18 - DECORADORES --------------------------------------- #
#
#   Es una función que recibe otra funcipon, la cual permite agregar mayor funcionalidad
#       a una función en concreto
#   Se podria decir que una función A reciba a una función B para crear una función C


# ---- Decoradores ------------------------------------------------------------------------------ #
#   Se crea una función decoradora, la cual recibe una función como parámetro
def decorador(func):                    # Función A
    def funcion_complementaria():       # Función B
        # En esta sección se agregara código para complementar
        print("\n\tSe ejecuto la función complemetaria")
        func()
        print("\tSe ejecuto la función complemetaria\n")

    return funcion_complementaria       # Función C
#   Para implementar la funcion con el decorador, basta con declararlo antes de la
#       funcion, entonces se vera relfejado


@decorador
def funcion():
    print("\tHola mundo")


funcion()


#   En caso de existir parámetros para la función que se desea decorar, es necesario
#       contemplar los argumentos en la función B
def decorador_2(func):
    def complementaria(*args, **kwargs):    # Se colocan los *argumentos
        print("\n\tSe ejecuto la función complemetaria 2")
        func(*args, **kwargs)               # Aqui tambien
        print("\tSe ejecuto la función complemetaria 2\n")
    return complementaria


@decorador_2
def suma(a, b):
    print("\tEl resultado es: {}".format(a + b))


suma(10, 5)

#   La estructura para la función que se pasa por parpámetro, debe contener la misma
#       sintaxis en la que se declara la fucnión
#   Ejemplos:
#   1) Con varios arguemntos de parámetros
#    func(a,b)
#
#       def funcion_complementaria(*args,**kwargs):
#           func(*args,**kwargs)
#
#   2) Función igualada a una variable
#   variable = func(a,b)
#
#       def funcion_complementaria(*args, **kwargs):
#           variable = func(*args,**kwargs)
#           return variable


# ---- Parámetros en Decoradores ---------------------------------------------------------------- #
#   Estos parámetros pueden ser utilizados para realizar o no ciertas iteraciones
#       dentro del decorador
def decorador_parametros(is_valid):
    def funcion_interna(func):
        #   Funciones auxiliares
        def pre_mensaje():
            print("\n\tSe ejecuto la función complemetaria")

        def post_mensaje():
            print("\tSe ejecuto la función complemetaria\n")

        #   Funcion complemetaria, la cual recibe a la función
        def funcion_complementaria(*args, **kwargs):
            if is_valid:    # Iteracion con el parámetro otorgado
                pre_mensaje()
            resultado = func(*args, **kwargs)
            post_mensaje()
            return resultado
        return funcion_complementaria
    return funcion_interna


#   Declaración del decorador con parámetro
@decorador_parametros(is_valid=False)
def funcion_principal(a, b):
    print("\tEl resultado es: {}".format(a + b))


funcion_principal(20, 54)
