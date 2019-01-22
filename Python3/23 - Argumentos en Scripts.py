# ------------------------------- 23 - ARGUMENTOS EN LOS SCRIPTS -------------------------------- #
#
#   Es posible que al ejecutar un script, se logre pasar uno o más argumentos a la hora de la
#       ejecución, dichos parámetros posicionaran al script en un estado incial
#
#   Como primer parámetro, se manda llamar a la función del scprit que se desea accesar
#

#   Para poder utilizar argumentos en los scripts, es necesario implentar la libreria sys
import sys

#   Para dar función al uso de parámetros en un script, se tendra que iniciar con la condicional
#       if __name__ = '__main__', previo a ello las funciones que se deseén realizar en base a los
#       argumentos que se pasan al scritp.
#   Para iterar sobre los agumentos, se utiliza 'sys.argv'
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("\n Es necesario colocar un argmuento al ejecutar el script.\n")
    else:
        if sys.argv[1] == 'help':
            print("\n Contacta con tu proovedor de servicios\n")
        else:
            print(sys.argv[1])
