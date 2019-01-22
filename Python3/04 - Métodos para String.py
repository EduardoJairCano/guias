# ---------------------------------- 04 - MÉTODOS PARA STRINGS ---------------------------------- #
#
#   Existen varias funciónes o métodos para trabajar con cadenas de texto
#   Métodos de Formato:
#   - format()
#   - lower()
#   - upper()
#   - title()
#   Métodos de Búsqueda:
#   - find()
#   - count()
#   Métodos de Sustitución
#   - replace()
#   - split()


# ---- Métodos de Formato ----------------------------------------------------------------------- #
#   Format - Con este método se puede asignar ciertas variables a un texto plano
a = "Eduardo Jair"
b = "Cano López"
#   Forma convencional
string_format = " El nombre del alumno es: {} {}".format(a, b)
print(string_format)
#   Forma con iteración entre variables
string_format = " El nombre del alumno es: {x} {y}".format(x=b, y=a)
print(string_format)
#   Lower - Este método arroja un nuevo String pero con minúsulas
print(string_format.lower())
#   Upper - Este método arroja un nuevo String pero con mayúsculas
print(string_format.upper())
#   Title - Arroja un nuevo String con formato de mayúsculas para las primeras letras de
#        cada palabra en la cadena
print(string_format.title())


# ---- Métodos de Búsqueda ---------------------------------------------------------------------- #
#   Find - Este método realiza una busquda en cierta variable con respecto a un
#       parámetro de busqueda que se le asigne, y devuelve una posición
pos = a.find('J')
print(" La posicion de la lera J en Eduardo Jair es: {}".format(pos))
#   Count - Devuelve la cantidad de veces que se repite cierto patrón
rep = a.count('a')
print(" La letra 'a', en el texto '{}' se repite: {} veces".format(a, rep))

# ---- Métodos de Sustitución ------------------------------------------------------------------- #
#   Replace - Este método sustituye ciertos caracteres por otro caracter en la función se
#        brindan como parámetros ('búsqueda', 'remplazo')
nuevo_string = a.replace('a', '4')
print(" Ahora el nombre es: {}".format(nuevo_string))
#   Split - Este método separa la cadena de texto en forma de arreglo, tomando como
#       parámetro de división el patrón que se asigne en la función
arreglo = a.split(' ')
print(arreglo)
