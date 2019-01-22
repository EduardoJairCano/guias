# ---------------------------------------- 02 - VARIABLES --------------------------------------- #
#
#   Espacios de memoria RAM que almacenan datos
#   - Caracteres
#   - Cadena de caracteres
#   - Números enteros y reales
#   - Boleanos


# ---- Caracteres y Cadenas de Caracteres ------------------------------------------------------- #
#   Declaración de variables para caracteres, texto entre comillas
cadena = "Cadena de texto"
print(cadena)
print("\n Tenemos una : ", cadena)
#   Manera correcta de crear vairables recomendable. variables en minisculas, en caso de
#       ser una variable larga se puede utilizar guien bajo: variable_a


# ---- Números Enteros y Reales ----------------------------------------------------------------- #
#   Los números enteros, pueden llegar de -9’233,372’036,855’775,808 al
#       9’233,372’036,855’775,807
numero_entero = 10
print("\n Número entero: ", numero_entero)
#   Los números reales o flotantes, los cuales cuentan con las mismas dimensiones que los
#       números enteros
numero_real = 25.8
print("\n Número real: ", numero_real)

# ---- Operadores Aritméticos ------------------------------------------------------------------- #
a = 10
b = 2.4
c = 32
d = .595

# Suma
print("\n Suma\n a+b = ", a+b)
# Resta
print("\n Resta\n c-12 = ", c-12)
# Multiplicación
print("\n Multiplicación\n d*b = ", d*b)
# División
print("\n División\n a//b = ", a//b)  # resultado con número entero
print("\n División con decimales\n a/b = ", a/b)  # resultado con decimales

# Módulo
print("\n Módulo\n 26 mod 5 = ", 26 % 5)
print("\n Módulo\n 4 mod 2 = ", 4 % 2)
# Exponencial -  en caso de querer cambiar la potencia se cambia el número
print("\n Potencia\n a**2 = ", a**2)

# ---- Boleanos --------------------------------------------------------------------------------- #
#   Estas variables solo cuentan con dos valores posibles True y False
