# ------------------------------------- 12 - FUNCIONES 01 --------------------------------------- #
#
#   Se puede definir como un conjunto de n operaciones para llegar a un resultado final,
#       la cual pueda o no repetirse n veces posibles
#   Se realiza mediante la instrucción def más un nombre de función descriptivo para el
#       cuál, aplican las mismas reglas que para el nombre de las variables, seguido de
#       paréntesis de apertura y cierre.


# ---- Funciones -------------------------------------------------------------------------------- #

def factorial():  # ---- Función factorial, no iterable con el usuario -------------------------- #
    numero = 5
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    print(factorial)


factorial()  # Llamada de funcion


def factorial_usuario(numero):  # ---- Función factorial, iterable con el usuario --------------- #
    a = numero
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    print("\n El factorial de {} es {}".format(a, factorial))


numero = int(input("\n Ingresa un numero: "))
factorial_usuario(numero)  # Llamada de funcion


def factorial_usuario(numero):  # ---- Función factorial, iterable con el usuario y retorno de valor
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


numero = int(input("\n Ingresa un numero: "))
resultado = factorial_usuario(numero)  # Llamada de funcion
print("\n El factorial de {} es {}".format(numero, resultado))
