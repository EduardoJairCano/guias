# ------------------------------------- 13 - FUNCIONES 02 --------------------------------------- #


# ---- Funciones con varios parametros ---------------------------------------------------------- #
def suma(a, b, c):
    return a + b + c


resultado = suma(10, 20, 30)
print(resultado)


#   Es posible alterar el orden de los argumentos, asignando las variables dentro de los
#       paréntesis
def division(a, b):
    return a / b


resultado = division(b=20, a=100)
print(resultado)


#   Valores por default en funciones, es posible asignarlos desde la función
def multiplicacion(a, b=50):
    return a * b


resultado = multiplicacion(10)
print(resultado)


#   Retorno de multiples valores para una función, los cuales seran regresados en forma
#       de tupla
def multiples_valores():
    return "String", True, 1.0, ["a", "b"]


resultado = multiples_valores()
print(resultado)
#   La manera en que pudieran ser aprovechados estos resultados sería asignadolos a
#       variables independientes
a = resultado[0]
b = resultado[1]
c = resultado[2]
d = resultado[3]
print("\n [1]: {}\n [2]: {}\n [3]: {}\n [4]: {}\n".format(a, b, c, d))

#   Las funciones pueden ser asignadas a variables
multi = multiplicacion
resultado = multi(4, 5)
print(resultado)


#   Funciiones dentro de funciones
def formato_resultado(funcion):
    res = funcion(3, 15)
    print("\n El resultado es: {}".format(res))


formato_resultado(multiplicacion)
