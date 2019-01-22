#!usr/bin/python3
"""
----------------------------------- ESTRUCTURAS DE LOS MÓDULOS ------------------------------------
Aqui se pueden encontrar las funciones auxiliares para una Calculadora
"""
__author__ = "Eduardo Jair Cano López"
__coyright__ = "Copyright 2018, Guia Python3"
__credits__ = "Código facilito"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Eduarde Jair"
__email__ = "eduardojaircano@hotmail.com"
__status__ = "Developer"
# ------------------------------ 21.1 - MÓDULO AUXILIAR ----------------------------------------- #
#   Estructura de los módulos:
#   1 - En este archivo solo deben exisitir funciones
#   2 - Se debe integrar el interprete con el que se debe ejecutar, el cual debe ser
#       escriito en la primera linea:
#           !usr/bin/python3
#   3 - Colocar la documenatión del módulo, despues de la identificación del interprete
#   4 - Ingresar los metadatos
#
#   Para poder localizar los datos del módulo desde el shell, es neceario emplear ciertas
#       palabras reservadas:
#       - import NOMBRE_MÓDULO  - para trabajar sobre ese módulo
#       - help(NOMBRE_MÓDULO)   - arrojara ciertos datos sobre el módulo
#       - dir(NOMBRE_MÓDULO)    - muestra los posibles datos que pueda o no tener el módulo
#
#   Aqui se declaran las funciones para el módulo auxiliar


# ---- Funciones auxiliares --------------------------------------------------------------------- #
def suma(a, b):
    """ Regresa la suma de dos números """
    return a+b


def resta(a, b):
    """ Regresa la resta de dos números """
    return a-b


def multiplicacion(a, b):
    """ Regresa la multiplicacion de dos números """
    return a*b


def division(a, b):
    """ Regresa la division de dos números """
    return a/b
