# --------------------------------------- 20 - DOCSTRING ---------------------------------------- #
#
#   La documentación de un proyecto debe ser una de las buenas practicas con las que se
#       debe contemplar, esto para que sea entendible en un posible futuro dicho código


# ---- Documentación ---------------------------------------------------------------------------- #
#
def generador(*args):
    """ Recibe n cantidad de números y regresa el número, ademas de un True o False si es
        número es mayor que 5, esta documentación debe ser declarada en la primera línea
        de la función, dado que el interperte de python lo tomara como documentación.
    """
    for valor in args:
        yield valor, True if valor > 5 else False


#   En caso de querer leer la documentación con la que pueda contar una función, se
#       tendria que buscar por medio de __doc__ y el nombre por medio de __name__
nombre = generador.__name__
documentación = generador.__doc__
print("\n Nombre: {}".format(nombre))
print("\n Documentación: {}".format(documentación))
