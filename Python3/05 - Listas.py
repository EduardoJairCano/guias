# ----------------------------------------- 05 - LISTAS ----------------------------------------- #
#
#   Conjunto de datos, en los cuales se pueden almacenar todo tipo de datos
#   Se puede modificar su tamaño, cuentan con índices
#   Métodos de las listas
#   - append()
#   - insert()
#   - remove()
#   - pop()
#   - sort()
#   - extend()
#   - append()


# ---- Listas ----------------------------------------------------------------------------------- #
#   Se declara el nombre para la lista, y su contenido entre [], cada uno de los elementos
#       separado por
lista_letras = ["a", "b", "c", "d", "e"]
lista_numeros = [1, 2, 3, 4, 5, 6, 7]
lista_general = ["Hola", 10, True, "Eduardo Jair", "Python3", [4.1, 4.2, 4.3]]
#   -- Append() - Agregar elementos a la lista en la posición final
print(lista_letras)
lista_letras.append("f")
print(lista_letras,"\n")
#   -- Insert() - Agregar elementos a la lista,contenplando una posición en específico
#       parametros para insert(posición_para_insertar, elemento_a_insertar)
print(lista_numeros)
lista_numeros.insert(0,0)
print(lista_numeros,"\n")
#   -- Remove() - Eliminar elemento(s) específico(s) dentro de una lista
print(lista_general)
lista_general.remove("Eduardo Jair")
print(lista_general,"\n")
#   -- Pop() - Eliminar o extaer el último elemento de la lista, para extraerlo se
#       tendria que asignar a alguna variable
print(lista_numeros)
elemento = lista_numeros.pop()
print(lista_numeros)
print(" Elemento extraido por pop: {}\n".format(elemento))
#   -- Sort() - Organiza una lista desordenada, simpre que la lista contenga el mismo tipo
#        de variable
lista_desordenada = [2, 532, 1, 27, 346, 99, 210, 4, 78, 544, 2010, 2, 4]
print(lista_desordenada)
lista_desordenada.sort()
print(lista_desordenada)
#   Ordenar en orden descendente
lista_desordenada.sort(reverse= True)
print(lista_desordenada)
#   Prueba con listas con variables String
lista_desordenada_2 = ["Fernando","Carlos","Jair","Karla","Jose","Ana"]
print(lista_desordenada_2)
lista_desordenada_2.sort()
print(lista_desordenada_2)
#   -- Extend() - Agregar una lista a otra
lista_nueva = lista_letras
lista_nueva.extend(lista_numeros)
print("\n",lista_nueva)
#   -- Append() - Agregar el la nueva lista pero como un elemento tipo arreglo
c = lista_letras
c.append(lista_numeros)
print("\n",c)
