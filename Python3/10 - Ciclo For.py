# ----------------------------------------- 10 - FOR -------------------------------------------- #
#
#   Es un tipo de ciclo para iterar con las variables crear ciclos, tomando en cuenta los
#       ciclos que se van a realizar


# ---- For -------------------------------------------------------------------------------------- #
#   Se debe declarar for más la variable que va a iterar dentro de un conjunto de datos

# ---- Iterar listas - tuplas - strins - diccionarios ------------------------------------------- #
#   Lista - Previo a declarar una lista para trabajar, se reliza el ciclo for en el cual
#       dice que por cada elemento de la lista lo va a imprimir
lista = [1, 2, 3, 4, 5, 6, 7, 8]
for valor in lista:
    print(valor)

#   Tupla - Por medio de la función enumerate() se puede localizar el número de iteración
#       en el que se encuentra el ciclos
tupla = ("a", "b", "c", "d", "e")
for indice, valor in enumerate(tupla):
    print(" {} tiene el indice {}".format(valor, indice))

#   String - Es posible iterar strings, el resultado es el recorrido de cada uno de los
#       elementos que contiene el string
for valor in "Hola mundo":
    print(valor)

#   Diccionario - Las iteraciones en este caso seran declaradas por medio de que tipo de
#       dato se declare, puede ser .items() - .keys() - .values()
diccionario = {
    'clave_01': "Eduardo Jair",
    'clave_02': "Cano López",
    'clave_03': 25,
    'clave_04': ["Estudiante", "Trabajador"]
}
for llave, valor in diccionario.items():
    print(" La llave {} tiene el valor {}".format(llave, valor))

for valor in diccionario.keys():
    print(valor)

for valor in diccionario.values():
    print(valor)
