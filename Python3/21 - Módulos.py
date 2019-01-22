# ---------------------------------------- 21 - MÓDULOS ----------------------------------------- #
#
#   Cuando un programa ya cuenta con suficientes líneas de código, es necesario separar
#        el código en varios segmentos o MÓDULOS, los cuales podran ser utilizados entre
#        archivos.


# ---- Módulos ---------------------------------------------------------------------------------- #
#   En esta ocación se utilizara el módulo auxiliar Calculadora, el cual debe estar en el
#       mismo nivel que esta archivo, con la palabra reservada IMPORT se denomida el origen
#       de las posibles funciones auxiliares que se emplearan
import Calculadora

resultado = Calculadora.suma(10, 20)
print("\n Resultado de la suma: {}".format(resultado))

#   Al ejecutar este archivo, se creara un folder con un archivo de formato .pyc, el cual
#       sera generado por el interprete de python, el cual es un archivo compilado, esto
#       para reducir el tiempo en ejecución, asi que cada que se cree un módulo, se creara
#       un archivo compilado

#   Otra forma de declara un módulo, es por medio de la palabra resrvada FROM, en la cual
#       se realiza una localizacion más exacata de las funciones a utilizar
from Calculadora import resta
#   De esta manera no es necesario emplear a Calculadora como un objeto, sino que
#       directamente se llama a la función
resultado = resta(100, 30)
print("\n Resultado de la resta: {}".format(resultado))

#   En caso de querer modificar el nombre de la función importada, es posibles por medio
#        de la palabra AS, la cual asigna un nuevo nombre a la función
from Calculadora import multiplicacion as multi
resultado = multi(5, 60)
print("\n Resultado de la multipliacion: {}".format(resultado))
