# ----------------------------------------- 09 - WHILE ------------------------------------------ #
#
#   Es un tipo de ciclo para iterar con las variables cerrar ciclos, obtener valores


# ---- While ------------------------------------------------------------------------------------ #
#   Se debe declarar while más la condicional, y dentro de la función aumentar la variable
#       contador
contador = 0
while contador < 10:
    print(" El contador va en {}".format(contador))
    contador += 1
#   Pueden agregarse iteraciones condicionales entre iteraciones
    if contador == 7:
        print("\n El número 7 es mi favorito!!\n")
#   Puede agregarse un else para imprimir o realizar alguna operación cuando el
#       ciclo a terminado
else:
    print("El ciclo While a terminado \n")

# ---- Continue y Break ------------------------------------------------------------------------- #
#   Continue - en caso de cumplir alguna iteración o alguna condicional, y que el ciclo se
#       pause, es posible decirle al programa que continue
#   Break - en caso de llegar a un break, la iteración terminara y se saldra de la función
i = 0
while i < 5:
    print(" El contador va en {}".format(i))
    i += 1
    if i == 3:
        continue
    elif i == 4:
        print("El segundo ciclo While termino en {}\n".format(i))
        break

# ---- Banderas --------------------------------------------------------------------------------- #
#   Una manera más correcta de emplear un corte de función, es utilizar una salida por
#       bandera, la cual puede tomar un valor verdadero o falso
j = 0
bandera = True
while bandera:
    print(" El contador va en {}".format(j))
    j += 1
    if j == 5:
        print("El tercer ciclo While termino en {}\n".format(j))
        bandera = False
