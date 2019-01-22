# ------------------------------------- 08 - CONDICIONALES -------------------------------------- #
#
#   Son comparativas entre variables, las cuales pueden se pueden emplear para cerrar
#       ciclos, obtener valores,
#
#   Operadores Relacionales
#   ==  Si los valores de los 2 operadores son iguales la condición es True
#   !=  Si los valores de los 2 operadores no son iguales la condición es True
#    >  Si el valor de la izquierda es mayor que el de la derecha la condición es True
#    <  Si el valor de la izquierda es menor que el de la derecha la condición es True
#   >=  Si el valor de la izquierda es mayor o igual que el de la derecha la condición es True
#   <=  Si el valor de la izquierda es menor o igual que el de la derecha la condición es True
#
#   Operadores Lógicos
#   and  Selecionar dos valores para la condición
#   or   Selecionar entre dos valores para responder la condición
#   not  Negar la condición


# ---- Condicionales ---------------------------------------------------------------------------- #
#   La estructura se compone de la palabra reservada if seguido por la variable de
#       referencia para la compración
animal = "perro"
if animal == "perro":
    print("\n Son iguales\n")
else:
    print("\n No son iguales\n")
#   Se puede utilizar las condicionales de otra manera
mensaje = "\n Son iguales\n" if animal == "gato" else "\n No son iguales\n"
print(mensaje)

# ---- Doble Condiional ------------------------------------------------------------------------- #
#   En caso de exsitir una segunda condicional, se utilizaria la palabra reservada elif,
#       en la cual se escribiria la segunda condicional
fruta = "manzana"
if fruta == "platano":
    print("\n Son iguales\n")
elif fruta == "manzana":
    print("\n Siempre si son iguales\n")
else:
    print("\n No son iguales\n")

#   En caso de que se pretenda que una condicional se cumpla para el mayor de los casos,
#       se puede emplear la palabra reservada pass para que obtener una mejor idenficación
#       entre condicionales
carro = "golf"
if carro == "platano":
    pass
elif carro == "golf":
    print("\n Son el mismo carro\n")
else:
    print("\n No son iguales\n")


# ---- Operadores Lógicos ----------------------------------------------------------------------- #
#   Se pueden emplear para que las iteraciones condicionales sean más complejas
if 10 < 0 and 10 > 100:     # and - Deben cumplirse todas
    print("\n El valor es mayor que 0 y menor que 100\n")
elif 10 == 10 or 10 != 0:   # or - con que se cumpla una
    print("\n El valor puede ser 10\n")
else:
    print("\n El valor no estra entre los parametros\n")
