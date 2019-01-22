# --------------------------------------- 24 - EXEPCIONES --------------------------------------- #
#
#   Un excepción es un error que pueda o no ejecutarse dentro e un script aal momento de estar
#       ejecutandose, dichos errores deben contemplarse y evitarse
#

#   Una excepción puede considerarse tan simple como el informar cuando un script a concluido
print(4/2)
print(" La división ha concluido, por lo tanto el script tambien.\n")

#   La meta de las excepciones es evitar los errores, como por ejemplo en una división entre cero,
#       la cual no pueda ser posible, el interprete de Python arrojaría un error, para evitar esto,
#       se emplea una excepción por medio de las funciones "try", "except" y "finally".
#
#   Dentro del "try" encontraremos todas las iteraciones que se desean intentar, y en caso de no ser
#       posibles, ingresarias a la sección "except", en donde se ejecutaría el mensaje de error
try:
    print(3/0)
except ZeroDivisionError as er:
#   Para que la sección "except" este completa, es necesario emplear el tipo de error que se desea
#       evitar, en este caso, el tipo de error que arrojaría el interprete seria ZeroDivisionError
#   En caso de querer utilizar el nombre del error, es posible asigarlo a una variable
    print(er)
    print("¡No es posible divir entre cero!\n")

#   En caso de no concer el tipo de error que pueda arrojar una iteración, se puede emplear un valor
#       por defaulr, un "Exception"
try:
    lista = [1,3,5]
    print(lista[9])
except Exception as er:
    print(er)
    print("Ocurrio algun error, pero no se que\n")
#   Existe otro bloque que siempre se va a ejecutar, sin importar que tipo de error arroje la
#       iteración, por medio de "finally" podemos realizar dicha acción
finally:
    print("\n El script ahora si termino")
