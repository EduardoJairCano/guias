# -------------------------------------- 11 - COMPREHESION -------------------------------------- #
#
#   Proveen una forma de escribir bucles for más concisamente. Pueden ser útiles cuando
#       quieres crear nuevas listas a partir de listas existentes o iterables.
#   Forma
#       - Valor a agregar a la lista
#       - Ciclo for
#       - Auxiliar de iteración


# ---- Listas de Comprensión -------------------------------------------------------------------- #
#   Se realiza un ciclo for dentro de los [] de la lista, y con la ayuda la función range()
#       se creara la iteración, contemplando el punto de inicio hasta el punto final
#   La primera variable dentro de los [] sera el valor que se agregara a la lista
lista = [valor for valor in range(0, 101)]
print(lista)
#   La variable que se asigne a la lista puede ser de cualquier tipo
lista = ["valor" for valor in range(0, 20)]
print(lista)
#   Una lista con elementos en valores a un mod (mod 2 en esta ocación)
lista = [valor for valor in range(0, 101) if valor % 2 == 0]
print(lista)

# ---- Listas de Comprensión con Tuplas --------------------------------------------------------- #
tupla = tuple((valor for valor in range(0, 101) if valor % 2 != 0))
print(tupla)

# ---- Listas de Comprensión con Diccionarios --------------------------------------------------- #
diccionario = {indice: valor for valor, indice in enumerate(lista)}
print(diccionario)
