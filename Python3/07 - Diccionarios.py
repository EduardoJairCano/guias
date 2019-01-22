# -------------------------------------- 07 - DICCIONARIOS -------------------------------------- #
#
#   Conjunto de datos, en el cual se pueden almacenar todo tipo de datos, los DICCIONARIOS
#       no se rigen por un índice, cuentan con claves (key), por los cules se rigen cada
#       uno de los campos o elementos


# ---- Diccionarios ----------------------------------------------------------------------------- #
#   Se declara el nombre para el diccionario, y su contenido entre {}, dentro se colocan
#       los clave_campo:dato y separado por , entre elementos
diccionario = {
    'clave_01': "Eduardo Jair",
    'clave_02': "Cano López",
    'clave_03': 25,
    'clave_04': ["Estudiante", "Trabajador"]
}
print(diccionario, "\n")

# ---- Seleccionar ------------------------------------------------------------------------------ #
#   Para seleccionar algún elemento específico del diccionario, se tiene que la clave que
#       se desea visualizar entre []
print(diccionario['clave_02'], "\n")
#   En caso que no exista el campo clave en el diccionario, se puede asignar un valor de
#       retorno por medio de la función get('campo', valor_retorno)
dato = diccionario.get('Nombre', ' -No existe el dato-\n')
print(dato)

# ---- Agregar o Modificar ---------------------------------------------------------------------- #
#   Para modificar o agregar un campo en el diccionario, se tendra que colocar la (nueva)
#       clave entre [], seguido por el valor para dicho campo
#   Agregar
diccionario['clave_05'] = 8000.00
print(diccionario['clave_05'])
#   Modificar
diccionario['clave_03'] = 26
print(diccionario)

# ---- Eliminar --------------------------------------------------------------------------------- #
#   Por medio de la funcion del , en la cual se le brinda la clave de campo
del diccionario['clave_02']
print("\n", diccionario, "\n")


# ---- Obtener llaves y valores ----------------------------------------------------------------- #
#   Con el método keys(), se pueden obtener las llaves de un diccionario para poder iterar
#        con ellas, pero las regresaria en una variable solamente
llaves = diccionario.keys()
print(llaves)
#   Para obtener las llaves y poder iterar con ellas, se tendria que almacenar pero con la
#       función list(), la cual otorgara al arreglo los privilegios de una lista
llaves = list(diccionario.keys())
print("\n", llaves)
#   Este método funciona de igual manera para la obtención de los valores, pero seria con
#       el método values()
valores = list(diccionario.values())
print("\n", valores)
#   Tambien pueden ser almacenados en un tupla, con el método tuple()
valores_tupla = tuple(diccionario.values())
print("\n", valores_tupla)

# ---- Agregar Valores de un Diccionario a otro ------------------------------------------------- #
#   En caso de querer anexar llaves y valores de un diccionario a otro, podria hacerse de
#       la siguiente manera
diccionario_02 = {
    'clave_06': "Nuevo Dato",
    'clave_07': True
}
diccionario['clave_06'] = diccionario_02['clave_06']
diccionario['clave_07'] = diccionario_02['clave_07']
print("\n Diccionario:\n", diccionario)
print("\n Diccionario_02:\n", diccionario_02)
#   La manera más correcta seria por medio del método update
diccionario.update(diccionario_02)
print("\n\n", diccionario)
