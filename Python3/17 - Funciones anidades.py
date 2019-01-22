# ----------------------------------- 17 - FUNCIONES ANIDADAS  ---------------------------------- #
#   Son dos o más funciones que dependen una de otra, es decir una puede estar en función
#       de otra.
#   Normalmente la primera función, sirve para validar ciertos parametros, si las
#       condicionales planteadas resultan adecuadas entorno a la función, entonces se
#       llamara a la siguiente función


# ---- Funciones Anidadas ----------------------------------------------------------------------- #
#   La función auiliar servira para validar los parametros que se ingresen
def validacion(a, b):
    return a > 0 and b < 10


def multiplicacion(a, b):
    if validacion(a, b):    # Anidación de una función
        return a * b


#   En caso de ser posible, se imprimira en consola el valor True
print(multiplicacion(10, 5))


# ---- Clouser: Funciones que crean funciones --------------------------------------------------- #
#   Otra manera de representar una función anidada, tomando en cuenta el ahorro de recursos
#       es declarar la función auxiliar unicamente en la fucnión principal
#   De esta manera se ahorra memoría, las variables declaradas en la función principal
#       pueden ser iteradas en las sub funciones
def multiplicacion_anidada(a, b):
    def validacion_anidada():   # No es necesario declarar parámetros
        return a > 0 and b < 10
    if validacion_anidada():
        return a * b
#   En esta ocacion se tenria que imprimir en pantalla un valor None, dado que las
#       condicionales no se cumplen


print(multiplicacion_anidada(3, 11))


# ---- Funciones que reciben funciones ---------------------------------------------------------- #
#   Es posible qe una funcion pueda recibir a otra función, es una manera en que se
#       trabajo la anidación, pero de manera en que las funciones hacen referencia a
#       otras funciones

#   Se declara la funcion auxiliar para parar como parámetro
def funcion():
    #   La función INPUT realiza una escritura en una variable tipo String, la cual es
    #       ingresada por medio del teclado
    a = input("\n Ingrese un numero mayor a 0: ")
    b = input("\n Ingrese un numero menor a 10: ")
    #   Se realiza un casteo para declara la variable ingresada tipo String a Int
    a = int(a)
    b = int(b)

    def validacion_auxiliar():
        return a > 0 and b < 10

    if validacion_auxiliar():
        resultado = a*b
        print("\n El resultado es: {}\n".format(resultado))
    else:
        print("\n Los valores estan fuera de rango\n")

    return validacion_auxiliar


#   Se crea la función que recibe por parametro otra función
def llamar_funcion(func):
    resultado = func()
    print(resultado)    # Imprime si es posible o no la opreción


#   Se realzia una la asignación de la función auxiliar y despues se pasa como parámetro
#       a la función
nueva_funcion = funcion()
llamar_funcion(nueva_funcion)
